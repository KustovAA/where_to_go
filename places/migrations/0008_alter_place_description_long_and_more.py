# Generated by Django 4.1 on 2022-11-17 22:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_content_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Описание(полное)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание(краткое)'),
        ),
    ]
