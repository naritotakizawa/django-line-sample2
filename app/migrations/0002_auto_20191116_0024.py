# Generated by Django 2.2.7 on 2019-11-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linemessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='linemessage',
            name='text',
            field=models.TextField(blank=True, verbose_name='テキスト'),
        ),
    ]
