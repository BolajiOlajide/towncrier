# Generated by Django 2.2.3 on 2019-07-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towncrierapp', '0004_auto_20190718_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slackuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='slackuser',
            name='slack_id',
            field=models.CharField(max_length=60, primary_key=True, serialize=False, unique=True),
        ),
    ]
