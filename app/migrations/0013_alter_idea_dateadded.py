# Generated by Django 4.2.5 on 2023-09-26 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_idea_dateadded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='dateAdded',
            field=models.DateField(default=datetime.datetime(2023, 9, 26, 20, 1, 10, 264163, tzinfo=datetime.timezone.utc)),
        ),
    ]
