# Generated by Django 2.1.13 on 2019-10-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('show', models.BooleanField(default=False, verbose_name='Работает')),
                ('content', models.TextField(blank=True, verbose_name='Код тега')),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчики',
            },
        ),
    ]
