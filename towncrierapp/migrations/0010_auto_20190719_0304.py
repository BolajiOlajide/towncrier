# Generated by Django 2.2.3 on 2019-07-19 03:04

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('towncrierapp', '0009_activitylog_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=mdeditor.fields.MDTextField(),
        ),
    ]