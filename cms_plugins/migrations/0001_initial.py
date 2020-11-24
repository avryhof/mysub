# Generated by Django 3.1.3 on 2020-11-24 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import filer.fields.file
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('filer', '0012_file_mime_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticatedUserPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_authenticateduserpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('show_to', models.CharField(choices=[('authenticated_users', 'Users who are logged in.'), ('unauthenticated_users', 'Users who are not logged in.')], default='authenticated_users', max_length=100)),
                ('unauthenticated_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='DIVPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_divpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ExpanderPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_expanderpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('text_class', models.CharField(blank=True, choices=[('text-primary', 'Primary (blue)'), ('text-secondary', 'Secondary (dark gray)'), ('text-success', 'Success (green)'), ('text-danger', 'Danger (red)'), ('text-warning', 'Warning (yellow)'), ('text-info', 'Info (turquoise)'), ('text-light', 'Light (white)'), ('text-dark', 'Dark (black)'), ('text-body', 'Body (default color)'), ('text-muted', 'Muted (gray)'), ('text-white', 'White'), ('text-black-50', '50% Black'), ('text-white-50', '50% White')], max_length=50, null=True)),
                ('background_class', models.CharField(blank=True, choices=[('bg-primary', 'Primary (blue)'), ('bg-secondary', 'Secondary (dark gray)'), ('bg-success', 'Success (green)'), ('bg-danger', 'Danger (red)'), ('bg-warning', 'Warning (yellow)'), ('bg-info', 'Info (turquoise)'), ('bg-light', 'Light (white)'), ('bg-dark', 'Dark (black)'), ('bg-transparent', 'Transparent'), ('bg-gradient-primary', 'Primary Gradient (blue)'), ('bg-gradient-secondary', 'Secondary Gradient (dark gray)'), ('bg-gradient-success', 'Success Gradient (green)'), ('bg-gradient-danger', 'Danger Gradient (red)'), ('bg-gradient-warning', 'Warning Gradient (yellow)'), ('bg-gradient-info', 'Info Gradient (turquoise)'), ('bg-gradient-light', 'Light Gradient (white)'), ('bg-gradient-dark', 'Dark Gradient (black)')], max_length=50, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='HeadingPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_headingpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('tag_type', models.CharField(blank=True, choices=[('h1', 'Heading 1'), ('h2', 'Heading 2'), ('h3', 'Heading 3'), ('h4', 'Heading 4'), ('h5', 'Heading 5'), ('h6', 'Heading 6')], max_length=50, null=True)),
                ('text_class', models.CharField(blank=True, choices=[('text-primary', 'Primary (blue)'), ('text-secondary', 'Secondary (dark gray)'), ('text-success', 'Success (green)'), ('text-danger', 'Danger (red)'), ('text-warning', 'Warning (yellow)'), ('text-info', 'Info (turquoise)'), ('text-light', 'Light (white)'), ('text-dark', 'Dark (black)'), ('text-body', 'Body (default color)'), ('text-muted', 'Muted (gray)'), ('text-white', 'White'), ('text-black-50', '50% Black'), ('text-white-50', '50% White')], max_length=50, null=True)),
                ('background_class', models.CharField(blank=True, choices=[('bg-primary', 'Primary (blue)'), ('bg-secondary', 'Secondary (dark gray)'), ('bg-success', 'Success (green)'), ('bg-danger', 'Danger (red)'), ('bg-warning', 'Warning (yellow)'), ('bg-info', 'Info (turquoise)'), ('bg-light', 'Light (white)'), ('bg-dark', 'Dark (black)'), ('bg-transparent', 'Transparent'), ('bg-gradient-primary', 'Primary Gradient (blue)'), ('bg-gradient-secondary', 'Secondary Gradient (dark gray)'), ('bg-gradient-success', 'Success Gradient (green)'), ('bg-gradient-danger', 'Danger Gradient (red)'), ('bg-gradient-warning', 'Warning Gradient (yellow)'), ('bg-gradient-info', 'Info Gradient (turquoise)'), ('bg-gradient-light', 'Light Gradient (white)'), ('bg-gradient-dark', 'Dark Gradient (black)')], max_length=50, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_list', serialize=False, to='cms.cmsplugin')),
                ('list_type', models.CharField(choices=[('ol', 'Ordered List'), ('ul', 'Unordered List')], default='ul', max_length=10)),
                ('list_style_type', models.CharField(blank=True, choices=[('None', None), ('disc', 'Disc'), ('circle', 'Circle')], default='None', max_length=16, null=True)),
                ('ordered_list_type', models.CharField(blank=True, choices=[('None', None), ('1', 'Numbers'), ('A', 'Uppercase Letters'), ('a', 'Lowercase Letters'), ('I', 'Uppercase Roman Numerals'), ('i', 'Lowercase Roman Numerals')], default='None', max_length=64, null=True)),
                ('ordered_list_start', models.IntegerField(blank=True, default=None, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_listitem', serialize=False, to='cms.cmsplugin')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='NavMenuPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_navmenupluginconfig', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PlainTextPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_plaintextpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('text', models.TextField(blank=True, null=True)),
                ('text_class', models.CharField(blank=True, choices=[('text-primary', 'Primary (blue)'), ('text-secondary', 'Secondary (dark gray)'), ('text-success', 'Success (green)'), ('text-danger', 'Danger (red)'), ('text-warning', 'Warning (yellow)'), ('text-info', 'Info (turquoise)'), ('text-light', 'Light (white)'), ('text-dark', 'Dark (black)'), ('text-body', 'Body (default color)'), ('text-muted', 'Muted (gray)'), ('text-white', 'White'), ('text-black-50', '50% Black'), ('text-white-50', '50% White')], max_length=50, null=True)),
                ('background_class', models.CharField(blank=True, choices=[('bg-primary', 'Primary (blue)'), ('bg-secondary', 'Secondary (dark gray)'), ('bg-success', 'Success (green)'), ('bg-danger', 'Danger (red)'), ('bg-warning', 'Warning (yellow)'), ('bg-info', 'Info (turquoise)'), ('bg-light', 'Light (white)'), ('bg-dark', 'Dark (black)'), ('bg-transparent', 'Transparent'), ('bg-gradient-primary', 'Primary Gradient (blue)'), ('bg-gradient-secondary', 'Secondary Gradient (dark gray)'), ('bg-gradient-success', 'Success Gradient (green)'), ('bg-gradient-danger', 'Danger Gradient (red)'), ('bg-gradient-warning', 'Warning Gradient (yellow)'), ('bg-gradient-info', 'Info Gradient (turquoise)'), ('bg-gradient-light', 'Light Gradient (white)'), ('bg-gradient-dark', 'Dark Gradient (black)')], max_length=50, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SectionPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_sectionpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('blue_background', models.BooleanField(default=False)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SVGImagePluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_svgimagepluginconfig', serialize=False, to='cms.cmsplugin')),
                ('link', models.CharField(blank=True, help_text='URL Name, Page Slug, or external link', max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('target', models.CharField(blank=True, choices=[('_self', 'Same Tab/Window (normal)'), ('_blank', 'New Tab/Window'), ('_parent', 'Parent Frame'), ('_top', 'Full Window (break frames)')], max_length=50, null=True)),
                ('alt_text', models.CharField(max_length=255)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('svg_image', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='svgimage', to='filer.file')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BlockTagPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_blocktagpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('tag_type', models.CharField(blank=True, choices=[('article', 'ARTICLE'), ('aside', 'ASIDE'), ('container', 'CONTAINER'), ('div', 'DIV'), ('footer', 'FOOTER'), ('header', 'HEADER'), ('hgroup', 'HGROUP'), ('main', 'MAIN'), ('section', 'SECTION')], max_length=50, null=True)),
                ('text_class', models.CharField(blank=True, choices=[('text-primary', 'Primary (blue)'), ('text-secondary', 'Secondary (dark gray)'), ('text-success', 'Success (green)'), ('text-danger', 'Danger (red)'), ('text-warning', 'Warning (yellow)'), ('text-info', 'Info (turquoise)'), ('text-light', 'Light (white)'), ('text-dark', 'Dark (black)'), ('text-body', 'Body (default color)'), ('text-muted', 'Muted (gray)'), ('text-white', 'White'), ('text-black-50', '50% Black'), ('text-white-50', '50% White')], max_length=50, null=True)),
                ('background_class', models.CharField(blank=True, choices=[('bg-primary', 'Primary (blue)'), ('bg-secondary', 'Secondary (dark gray)'), ('bg-success', 'Success (green)'), ('bg-danger', 'Danger (red)'), ('bg-warning', 'Warning (yellow)'), ('bg-info', 'Info (turquoise)'), ('bg-light', 'Light (white)'), ('bg-dark', 'Dark (black)'), ('bg-transparent', 'Transparent'), ('bg-gradient-primary', 'Primary Gradient (blue)'), ('bg-gradient-secondary', 'Secondary Gradient (dark gray)'), ('bg-gradient-success', 'Success Gradient (green)'), ('bg-gradient-danger', 'Danger Gradient (red)'), ('bg-gradient-warning', 'Warning Gradient (yellow)'), ('bg-gradient-info', 'Info Gradient (turquoise)'), ('bg-gradient-light', 'Light Gradient (white)'), ('bg-gradient-dark', 'Dark Gradient (black)')], max_length=50, null=True)),
                ('show_background_image', models.BooleanField(default=False)),
                ('background_size_class', models.CharField(choices=[('auto', "Display the image at it's original size."), ('cover', 'Resize the image to cover the entire container.'), ('contain', 'Resize the image to make sure it is fully visible.'), ('percentage', 'Set a Percentage to zoom the image to.')], default='cover', max_length=30)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('background_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bt_bg_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
