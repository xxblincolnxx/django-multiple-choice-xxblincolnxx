# Generated by Django 3.0.4 on 2020-03-18 17:32

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0011_auto_20200318_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('figure_raw', '200x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
