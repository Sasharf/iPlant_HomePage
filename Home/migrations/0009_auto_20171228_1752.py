# Generated by Django 2.0 on 2017-12-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20171228_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorslogs',
            name='sync_time',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]
