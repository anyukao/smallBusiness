# Generated by Django 4.1.6 on 2023-06-16 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('abstractclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.abstractclass')),
            ],
            options={
                'verbose_name': 'Гражданство',
                'verbose_name_plural': 'Y| Гражданство',
            },
            bases=('students.abstractclass',),
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('abstractclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.abstractclass')),
            ],
            options={
                'verbose_name': 'Национальность',
                'verbose_name_plural': 'Y| Национальности',
            },
            bases=('students.abstractclass',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(blank=True, max_length=10, null=True, verbose_name='ПИН-код')),
                ('unique_code_user', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='уникальный код студента')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('number_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KG')),
                ('email', models.EmailField(max_length=254)),
                ('data_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'мужчина'), ('F', 'женщина'), ('OTHER', 'другое')], default='M', max_length=8, verbose_name='Пол')),
                ('images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('citizenship', models.CharField(max_length=255, null=True, verbose_name='Гражданство')),
                ('family_members', models.TextField(blank=True, null=True, verbose_name='Члены семьи')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Статус пользователя')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national', to='students.nationality', verbose_name='Национальность')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'A| Студент',
            },
        ),
        migrations.CreateModel(
            name='PassportDataS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typedoc', models.CharField(max_length=255, null=True, verbose_name='Вид документа')),
                ('serial', models.CharField(blank=True, max_length=255, null=True, verbose_name='Серия')),
                ('number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер паспорта')),
                ('issued_by', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кем выдан')),
                ('date_of_issue', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дата выдачи')),
                ('date_end', models.CharField(blank=True, max_length=255, null=True, verbose_name='Дата окончания')),
                ('inn', models.CharField(blank=True, max_length=255, null=True, verbose_name='ИНН')),
                ('document', models.FileField(blank=True, null=True, upload_to='', verbose_name='Документ')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='passport_datas', to='students.student')),
            ],
            options={
                'verbose_name': 'Паспортные данные',
                'verbose_name_plural': 'A| Паспортные данные студентов',
            },
        ),
        migrations.CreateModel(
            name='EntranceStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_status', models.CharField(blank=True, max_length=250, null=True, verbose_name='Учебный статус')),
                ('institute', models.CharField(blank=True, max_length=255, null=True, verbose_name='Институт')),
                ('group', models.CharField(blank=True, max_length=255, null=True, verbose_name='Группа')),
                ('direction', models.CharField(blank=True, max_length=255, null=True, verbose_name='Направление')),
                ('date_of_receipt', models.DateField(blank=True, null=True, verbose_name='Дата Поступления')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Дата Выпуска')),
                ('form_of_training', models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма обучения')),
                ('contract', models.CharField(blank=True, max_length=255, null=True, verbose_name='Договор')),
                ('document_contract', models.FileField(blank=True, null=True, upload_to='Документ', verbose_name='Документ')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrancestudents', to='students.student')),
            ],
            options={
                'verbose_name': 'Движение студента',
                'verbose_name_plural': 'B| Движение студента',
            },
        ),
    ]
