# Generated by Django 4.1.6 on 2023-06-18 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_passportdatas_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PassportDataS',
        ),
    ]
