# Generated by Django 4.1.6 on 2023-06-16 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_languageproficiencystudent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passportdatas',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pdata', to='students.student'),
        ),
    ]
