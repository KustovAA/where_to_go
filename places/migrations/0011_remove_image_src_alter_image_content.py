# Generated by Django 4.1 on 2022-11-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_description_short'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='src',
        ),
        migrations.AlterField(
            model_name='image',
            name='content',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
    ]
