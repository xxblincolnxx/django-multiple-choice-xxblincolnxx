# Generated by Django 3.0.4 on 2020-03-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0009_auto_20200317_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='figure_raw',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
