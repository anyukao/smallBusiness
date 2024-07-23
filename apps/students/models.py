from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from .utils import generate_code, post_generate_unique_username, triple_latter

# from apps_logic.univer.models import *



class AbstractClass(models.Model): 
    """
    Абстрактный класс для моделей Гражданство, Нацианальности
    """
    title = models.CharField(unique=True, verbose_name="Название", max_length=255)

    def __str__(self):
        return self.title
        

class Student(models.Model):
    """
    Модель студента которая подтягивает данные из внешней API
    """
    OTHER = "OTHER"

    GENDER = (
        ("M", 'мужчина'),
        ("F", 'женщина'),
        (OTHER, "другое")
    )

    MARRIED = 'Married'
    SINGLE = 'Single'
    WIDOWED = 'Widowed'
    DIVORCED = 'Divorced'

    MARITAL_STATUS = (
        (SINGLE, "не замужем / не женат"),
        (MARRIED, "замужем / женат"),
        (DIVORCED, "разведен / разведена"),
        (WIDOWED, "вдовец / вдова")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    pin =  models.CharField(verbose_name="ПИН-код",max_length=10,blank=True,null=True)
    unique_code_user = models.CharField(unique=True, verbose_name="уникальный код студента",
                                        blank=True, null=True, max_length=255)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    last_name = models.CharField(max_length=255, verbose_name="Отчество")
    number_phone = PhoneNumberField(region="KG")
    email = models.EmailField()
    data_of_birth = models.DateField()
    nationality = models.ForeignKey(to="Nationality", on_delete=models.PROTECT,
                                    related_name="national", verbose_name="Национальность", blank=True,null=True)
    gender = models.CharField(choices=GENDER, default="M", max_length=8, verbose_name="Пол")
    images = models.ImageField("Фотография", blank=True, null=True)
    citizenship = models.CharField( verbose_name="Гражданство",max_length=255, null=True)
   
    family_members = models.TextField(blank=True, null=True, verbose_name="Члены семьи")
    create_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255, verbose_name="Статус пользователя", null=True, blank=True)
    
    @property
    def full_name(self):
        
        return self.surname + " " + self.first_name + " " + self.last_name

    def generate_unique_user(self):
        if not self.unique_code_user:
            self.unique_code_user = self.passport_datas.inn + triple_latter(self.full_name) + \
                                    generate_code(4, '0123456789') + str(self.create_date).replace("-", "")
            self.save()
            return True
        return False

    def get_absolute_url(self):
        return reverse("personal_datas",kwargs={"slug":self.url})
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "A| Студент"


class Nationality(AbstractClass):
    class Meta:
        verbose_name = "Национальность"
        verbose_name_plural = "Y| Национальности"


class Citizenship(AbstractClass):
    class Meta:
        verbose_name = "Гражданство"
        verbose_name_plural = "Y| Гражданство"
        

class PassportDataS(models.Model):
    """
    модель паспортных данных взятые из третей API
    """

    student = models.OneToOneField(Student, on_delete=models.PROTECT, related_name="passport_datas")
    typedoc = models.CharField(max_length=255, verbose_name="Вид документа", null=True)
    serial = models.CharField(max_length=255, verbose_name="Серия", null=True, blank=True)
    number = models.CharField(verbose_name="Номер паспорта", max_length=255, null=True, blank=True)
    issued_by = models.CharField(max_length=255, verbose_name="Кем выдан", null=True, blank=True)
    date_of_issue = models.CharField(max_length=255, verbose_name="Дата выдачи", null=True, blank=True)
    date_end = models.CharField(max_length=255, verbose_name="Дата окончания", null=True, blank=True)
    inn = models.CharField(verbose_name="ИНН", max_length=255, null=True, blank=True)
    document = models.FileField(verbose_name="Документ", blank=True, null=True)

    class Meta:
        verbose_name = "Паспортные данные"
        verbose_name_plural = "A| Паспортные данные студентов"

    def __str__(self):
        return self.student.full_name


post_save.connect(post_generate_unique_username, sender=PassportDataS)

class EntranceStudents(models.Model):

    #Поступление студента

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True ,null=True, related_name="entrancestudents")
    academic_status = models.CharField("Учебный статус",max_length=250,blank=True , null=True)
    institute = models.CharField(max_length=255, verbose_name="Институт",blank=True , null=True)
    group = models.CharField(max_length=255, verbose_name="Группа",blank=True , null=True)
    direction = models.CharField(max_length=255, verbose_name="Направление",blank=True , null=True)
    date_of_receipt = models.DateField("Дата Поступления",blank=True , null=True)
    date_end = models.DateField("Дата Выпуска",blank=True , null=True)
    form_of_training = models.CharField(max_length=255, verbose_name="Форма обучения", blank=True , null=True)
    contract = models.CharField(max_length=255, verbose_name="Договор", blank=True , null=True)
    document_contract = models.FileField(upload_to="Документ", verbose_name="Документ", blank=True , null=True)
    def __str__(self):
        return self.student.full_name + "  ---  " + self.name_fam

    class Meta:
        verbose_name = "Движение студента"
        verbose_name_plural = "B| Движение студента"

# class PlaceOfBirthStudents(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="place_of_birthstudents")
#     country = models.CharField(verbose_name="Страна", max_length=255, blank=True, null=True)
#     region=models.CharField(verbose_name="Область", max_length=255, blank=True, null=True)
#     village=models.CharField(verbose_name="Село", max_length=255, blank=True, null=True)
#     city=models.CharField(verbose_name="Город", max_length=255, blank=True, null=True)
#     district=models.CharField(verbose_name="Район", max_length=255, blank=True, null=True)
#     street=models.CharField(verbose_name="Улица", max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.student.full_name
#     class Meta:
#         verbose_name = "Место рождение студента"
#         verbose_name_plural = "Y| Место рождение студента"
        
#
# class PlaceOfResidenceStudents(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="placeofresidencestudents")
#     country = models.CharField(verbose_name="Страна", max_length=255, blank=True, null=True)
#     region=models.CharField(verbose_name="Область", max_length=255, blank=True, null=True)
#     village=models.CharField(verbose_name="Село", max_length=255, blank=True, null=True)
#     city=models.CharField(verbose_name="Город", max_length=255, blank=True, null=True)
#     district=models.CharField(verbose_name="Район", max_length=255, blank=True, null=True)
#     street=models.CharField(verbose_name="Улица", max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.student.full_name
#     class Meta:
#         verbose_name = "Место жительства студента"
#         verbose_name_plural = "Y| Место жительства студента"

# class LanguageProficiencyStudents(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="languageproficiencystudents")
#     statelanguage = models.CharField(verbose_name="Знание государственного языка", max_length=255, blank=True, null=True)
#     languagesem=models.CharField(verbose_name="Язык", max_length=255, blank=True, null=True)
#     levellang=models.CharField(verbose_name="Уровень знания языка", max_length=255, blank=True, null=True)
#
#
#     def __str__(self):
#         return self.student.full_name + " --- " + self.languagesem  + " --- " + self.levellang
#     class Meta:
#         verbose_name = "Знание языков"
#         verbose_name_plural = "Y| Знание языков"
#
# class EducationStudents(models.Model):
#     """
#     Образование студента
#     """
#     student = models.ForeignKey(Student, on_delete=models.SET_NULL,  blank=True, null=True, related_name="educationstudents")
#     type_of_document = models.CharField(verbose_name="Вид документа", max_length=255)
#     serial = models.CharField(max_length=255, verbose_name="Серия", null=True)
#     number = models.IntegerField(default=0, verbose_name="Номер")
#     issued_by = models.CharField(max_length=255, verbose_name="Кем выдан")
#     date_of_issue = models.DateField(verbose_name="Дата выдачи")
#     documents = models.FileField(verbose_name="Документ", blank=True, null=True)
#
#
#     class Meta:
#         verbose_name = "Образование"
#         verbose_name_plural = "Y| Образовании"
#
#     def __str__(self):
#         return self.student.full_name
#
# class FamilyMembersStudents(models.Model):
#
#     #Состав семьи
#
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True ,null=True, related_name="family")
#     name_fam = models.CharField("Степень родства",max_length=250)
#     first_name = models.CharField(max_length=255, verbose_name="Имя",blank=True , null=True)
#     surname = models.CharField(max_length=255, verbose_name="Фамилия",blank=True , null=True)
#     last_name = models.CharField(max_length=255, verbose_name="Отчество",blank=True , null=True)
#     d_o_b = models.DateField("Дата рождения")
#     title_place_work = models.CharField(max_length=255, verbose_name="Место работы", null=True, blank=True)
#     position = models.CharField(max_length=255, verbose_name="Должность", blank=True , null=True)
#     number_phone = PhoneNumberField(region="KG")
#
#     def __str__(self):
#         return self.student.full_name + "  ---  " + self.name_fam
#
#     class Meta:
#         verbose_name = "Состав семьи"
#         verbose_name_plural = "Y| Состав семьи"
#
# class ScheduleStudents(models.Model):
#     """
#     Расписание студента
#     """
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True ,null=True, related_name="schedulestudents")
#     subject = models.ManyToManyField(to=LesUni,  related_name='subject')
#     type_of_lesson = models.ForeignKey(to=TypeOfLesson, verbose_name="Вид предмета", on_delete=models.CASCADE ,  related_name='type_of_lesson')
#     group = models.ForeignKey(to=Groups, on_delete=models.SET_NULL, null=True,  related_name='group')
#     semester = models.CharField(verbose_name="Семестр", max_length=255, blank=True ,null=True )
#
#     def __str__(self):
#         return self.student.full_name
#
#     class Meta:
#         verbose_name = "Расписание студента"
#         verbose_name_plural = "C| Расписание студента"
#
#
# class EntranceStudents(models.Model):
#
#     #Поступление студента
#
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True ,null=True, related_name="entrancestudents")
#     academic_status = models.CharField("Учебный статус",max_length=250)
#     faculty = models.CharField(max_length=255, verbose_name="Факультет",blank=True , null=True)
#     Direction = models.CharField(max_length=255, verbose_name="Направление",blank=True , null=True)
#     admission_score = models.CharField(max_length=255, verbose_name="Балл поступления",blank=True , null=True)
#     date_of_receipt = models.DateField("Дата Поступления")
#     title_place_work = models.CharField(max_length=255, verbose_name="Место работы", null=True, blank=True)
#     form_of_training = models.CharField(max_length=255, verbose_name="Форма обучения", blank=True , null=True)
#     Contract = models.CharField(max_length=255, verbose_name="Договор", blank=True , null=True)
#     document_contract = models.FileField(upload_to="Документ", verbose_name="Документ")
#     def __str__(self):
#         return self.student.full_name + "  ---  " + self.name_fam
#
#     class Meta:
#         verbose_name = "Поступление студента"
#         verbose_name_plural = "B| Поступление студента"
#
#
# class TrainingStudents(models.Model):
#
#     #Обучение студента
#
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True ,null=True, related_name="trainingstudents")
#     group = models.CharField("Группа",max_length=250)
#     сredit_card_number = models.CharField(max_length=255, verbose_name="Номер зачетки",blank=True , null=True)
#     student_id_number = models.CharField(max_length=255, verbose_name="Номер студенческого",blank=True , null=True)
#     сurriculum = models.CharField(max_length=255, verbose_name="Учебный план",blank=True , null=True)
#
#     def __str__(self):
#         return self.student.full_name + "  ---  " + self.name_fam
#
#     class Meta:
#         verbose_name = "Обучение студента"
#         verbose_name_plural = "Y| Обучение студента"
#
#
#
# class LanguageProficiencyStudent(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="languageproficiencystudent")
#     statelanguage = models.CharField(verbose_name="Знание государственного языка", max_length=255, blank=True, null=True)
#     languagesem=models.CharField(verbose_name="Язык", max_length=255, blank=True, null=True)
#     levellang=models.CharField(verbose_name="Уровень знания языка", max_length=255, blank=True, null=True)
#
#
#     def __str__(self):
#         return self.student.full_name + " --- " + self.languagesem  + " --- " + self.levellang
#     class Meta:
#         verbose_name = "Знание языков"
#         verbose_name_plural = "Y| Знание языков"
        