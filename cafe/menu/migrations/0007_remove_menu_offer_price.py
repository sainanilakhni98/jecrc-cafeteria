# Generated by Django 2.2.3 on 2019-09-25 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='offer_price',
        ),
    ]
