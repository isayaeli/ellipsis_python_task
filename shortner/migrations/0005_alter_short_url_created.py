# Generated by Django 4.0.5 on 2022-06-10 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0004_short_url_is_expired_alter_short_url_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_url',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 10, 8, 34, 9, 156332)),
        ),
    ]
