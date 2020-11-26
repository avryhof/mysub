import base64
import os

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from utilities.files import file_get_contents, get_mime_type
from utilities.helpers import make_list


def send_multipart_email(subject_str, to_list, from_str, template_path, context_dict, **kwargs):
    """Send a single html email message (which can be sent to multiple recipients).

        subject_str = String to use as email subject
        to_list = list of recipient email address strings
        from_str = string to use as the from email address
        template_path = path, from webroot to the email template to use, .html type
        context_dict = dictionary defining any variables that are required to fully render the template."""
    request = kwargs.get("request", None)
    attachments = kwargs.get("attachments", False)

    if context_dict is None:
        context_dict = {}

    if not isinstance(from_str, str):
        from_str = settings.DEFAULT_FROM_EMAIL

    html_template_path = "%s.html" % template_path
    text_template_path = "%s.txt" % template_path

    html_content = get_template(html_template_path).render(context_dict, request)
    text_content = get_template(text_template_path).render(context_dict, request)

    message = EmailMultiAlternatives(subject_str, text_content, from_str, to_list)
    message.attach_alternative(html_content, "text/html")

    if attachments:
        for attachment in make_list(attachments):
            att_data = file_get_contents(attachment)
            base64_attachment = base64.b64encode(att_data).decode()

            message.attach(os.path.basename(attachment), base64_attachment, get_mime_type(attachment))

    result = message.send()

    return result
