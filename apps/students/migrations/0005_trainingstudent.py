# Generated by Django 4.1.6 on 2023-06-16 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_familymembersstudents_educationstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=250, verbose_name='Группа')),
                ('сredit_card_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер зачетки')),
                ('student_id_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер студенческого')),
                ('сurriculum', models.CharField(blank=True, max_length=255, null=True, verbose_name='Учебный план')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainingstudents', to='students.student')),
            ],
            options={
                'verbose_name': 'Обучение студента',
                'verbose_name_plural': 'Y| Обучение студента',
            },
        ),
    ]
