# Generated by Django 3.2.16 on 2022-11-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_alter_response_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Последнее обновление'),
        ),
    ]
