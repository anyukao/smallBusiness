# Generated by Django 4.1.6 on 2023-06-16 11:57

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_placeofbirthstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMembersStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fam', models.CharField(max_length=250, verbose_name='Степень родства')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('d_o_b', models.DateField(verbose_name='Дата рождения')),
                ('title_place_work', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('number_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KG')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family', to='students.student')),
            ],
            options={
                'verbose_name': 'Состав семьи',
                'verbose_name_plural': 'Y| Состав семьи',
            },
        ),
        migrations.CreateModel(
            name='EducationStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_document', models.CharField(max_length=255, verbose_name='Вид документа')),
                ('serial', models.CharField(max_length=255, null=True, verbose_name='Серия')),
                ('number', models.IntegerField(default=0, verbose_name='Номер')),
                ('issued_by', models.CharField(max_length=255, verbose_name='Кем выдан')),
                ('date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('documents', models.FileField(blank=True, null=True, upload_to='', verbose_name='Документ')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='educationstudents', to='students.student')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Y| Образовании',
            },
        ),
    ]
