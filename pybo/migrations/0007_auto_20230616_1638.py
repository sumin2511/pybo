# Generated by Django 3.1.3 on 2023-06-16 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_question_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='modify_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='modify_date',
        ),
    ]