# Generated by Django 2.2.3 on 2019-07-18 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('towncrierapp', '0003_auto_20190718_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slackuser',
            old_name='email',
            new_name='handle',
        ),
        migrations.RemoveField(
            model_name='slackuser',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='slackuser',
            name='lastname',
        ),
    ]