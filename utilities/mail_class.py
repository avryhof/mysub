import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from os.path import basename

COMMASPACE = ", "


class Mailer(object):
    message = None
    send_to = []
    send_from = None

    subject = None
    body = None
    alt_body = None
    html_body = None

    host = "127.0.0.1"

    def __init__(self):
        self.message = MIMEMultipart()

    def set_from(self, from_address):
        self.send_from = from_address

    def add_address(self, to_address):
        self.send_to.append(to_address)

    def add_attachment(self, file_name, optional_name=False):
        base_filename = basename(file_name) if not optional_name else optional_name

        with open(file_name, "rb") as fh:
            part = MIMEApplication(fh.read(), Name=base_filename)

        # After the file is closed
        part["Content-Disposition"] = 'attachment; filename="%s"' % base_filename
        self.message.attach(part)

    def text_to_html(self, text):
        message_text = text.replace("\n", "<br>")
        self.html_body = "<html><head></head><body>%s</body></html>" % message_text

        return self.html_body

    def send(self):
        self.message["From"] = self.send_from
        self.message["To"] = COMMASPACE.join(self.send_to)
        self.message["Date"] = formatdate(localtime=True)
        self.message["Subject"] = self.subject

        message_text = self.alt_body
        self.message.attach(MIMEText(self.alt_body))

        if not self.html_body:
            self.text_to_html(message_text)

        message_html = self.html_body
        self.message.attach(MIMEText(message_html, "html"))

        smtp = smtplib.SMTP(self.host)
        smtp.sendmail(self.send_from, self.send_to, self.message.as_string())
        smtp.close()
