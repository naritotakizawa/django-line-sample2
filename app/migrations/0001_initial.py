# Generated by Django 2.2.2 on 2019-07-31 04:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinePush',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True, verbose_name='ユーザーID')),
                ('display_name', models.CharField(blank=True, max_length=255, verbose_name='表示名')),
            ],
        ),
        migrations.CreateModel(
            name='LineMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='テキスト')),
                ('is_admin', models.BooleanField(default=True, verbose_name='このメッセージは管理者側の発言か')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('push', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.LinePush', verbose_name='プッシュ先')),
            ],
        ),
    ]
