# Generated by Django 3.1.3 on 2020-11-24 23:43

import colorfield.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields.json
import djangocms_attributes_field.fields
import djangocms_icon.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionHeaderPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_freedom_sectionheaderpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('heading_prefix', models.CharField(blank=True, max_length=100, null=True)),
                ('emphasis_word', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_heading', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TopBarPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_freedom_topbarpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('link', models.CharField(blank=True, help_text='URL Name, Page Slug, or external link', max_length=255, null=True)),
                ('target', models.CharField(blank=True, choices=[('_self', 'Same Tab/Window (normal)'), ('_blank', 'New Tab/Window'), ('_parent', 'Parent Frame'), ('_top', 'Full Window (break frames)')], max_length=50, null=True)),
                ('prompt_text', models.CharField(blank=True, default='Have any questions?', max_length=150, null=True)),
                ('phone', models.CharField(blank=True, default='123-456-7890', max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('link_email', models.BooleanField(default=False, help_text='Best practice is not to link the email address.')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Login Button Text')),
                ('foreground_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('background_color', colorfield.fields.ColorField(default='#14BDEE', max_length=18)),
                ('login_foreground_color', colorfield.fields.ColorField(default='#14BDEE', max_length=18)),
                ('login_background_color', colorfield.fields.ColorField(default='#384158', max_length=18)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PortfolioItemPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_freedom_portfolioitempluginconfig', serialize=False, to='cms.cmsplugin')),
                ('link', models.CharField(blank=True, help_text='URL Name, Page Slug, or external link', max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('target', models.CharField(blank=True, choices=[('_self', 'Same Tab/Window (normal)'), ('_blank', 'New Tab/Window'), ('_parent', 'Parent Frame'), ('_top', 'Full Window (break frames)')], max_length=50, null=True)),
                ('sub_heading', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', djangocms_icon.fields.Icon(blank=True, default='', max_length=255, verbose_name='Icon')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pfi_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BannerSectionPluginConfig',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cms_plugins_freedom_bannersectionpluginconfig', serialize=False, to='cms.cmsplugin')),
                ('text_prefix', models.CharField(blank=True, max_length=100, null=True)),
                ('rotate_words', django_extensions.db.fields.json.JSONField(default=dict)),
                ('transition_delay', models.IntegerField(default='2000', validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)])),
                ('subheading', models.CharField(blank=True, max_length=100, null=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict)),
                ('background_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bg_image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
