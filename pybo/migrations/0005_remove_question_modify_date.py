# Generated by Django 3.1.3 on 2023-06-16 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_auto_20230616_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='modify_date',
        ),
    ]