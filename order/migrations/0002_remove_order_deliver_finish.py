# Generated by Django 3.2.2 on 2022-10-26 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='deliver_finish',
        ),
    ]
