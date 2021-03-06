# Generated by Django 2.1.13 on 2019-10-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название для людей')),
                ('name', models.SlugField(help_text='писать латинскими без пробелов и без {{', max_length=255, verbose_name='Название в шаблоне')),
                ('default', models.TextField(blank=True, null=True, verbose_name='Значение стандартное')),
            ],
            options={
                'verbose_name': 'Параметр шаблона',
                'verbose_name_plural': 'Параметры шаблона',
            },
        ),
        migrations.AlterUniqueTogether(
            name='param',
            unique_together={('name',)},
        ),
    ]
