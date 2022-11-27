# Generated by Django 3.2.16 on 2022-11-27 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блок',
            },
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Дорожная карта',
                'verbose_name_plural': 'Дорожные карты',
            },
        ),
        migrations.CreateModel(
            name='SiteParam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.TextField(blank=True, null=True, verbose_name='Параметры парсера')),
                ('block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roadmaps.block', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Параметры сайта',
                'verbose_name_plural': 'Параметры сайтов',
            },
        ),
    ]