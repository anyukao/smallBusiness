import smtplib
from email.mime.text import MIMEText
from random import randint

from django.contrib.auth.decorators import (login_required,
                                            permission_required,
                                            user_passes_test)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

# from apps_logic.country.models import *
from apps_logic.employees.models import Employee, PassportData
from config.service import get_summ_alerts, get_summ_applications

# from .forms import *
from .models import *


def send_email(login, passw, useremail ):
    
    sender = "kstusgpkg@gmail.com"
    password = "Lee4436s"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    
    try:
        
        server.login(sender, password)
        msg=MIMEText("Ваш логин для входа в sgp.kstu.kg: " + login + "    Пароль: " + passw)
        server.sendmail(sender, useremail, msg.as_string())
        #server.sendmail(sender, useremail, f"Subject: Код для входа в SGP-KSTU!\n{messages}" )

        return "Сообщение отрпавлено на почту"
    except Exception as _ex:
        return f"{_ex}\nОшибка добавления"


def is_student(user):
    return user.groups.filter(name='студент').exists()



@login_required
@user_passes_test(is_student)
def KSTUstudentaccount(request, id):
        user = User.objects.get(id=id)
        student = Student.objects.all()
        innt = PassportDataS.objects.all()
        
        for i in innt:
            iins=str(i.inn)
            if iins == user.username:
                student=Student.objects.get(id=i.employee_id)
                entry = Student.objects.get(pk=i.employee_id)
              
      
            
        if request.method == "POST":
            entry = Student.objects.get(pk='firstkay')
            queryimeag = request.POST.get('Photo')  
            
            
            cheese_imeag = Student.objects.get(imeag = queryimeag)
            entry.imeag = cheese_imeag
            entry.save()
        summr = get_summ_alerts(request)
        summs = get_summ_applications()
        context = {"summr": summr, "summs": summs,"user": user, "student":student}
        return render(request,"students/home/studentaccount.html", context )


def is_member(user):
    return user.groups.filter(name='отдел_кадров_студентов').exists()


@login_required
@user_passes_test(is_member)
def KSTUpersonalaccounts(request, id):
        user = User.objects.get(id=id)
        personal = Employee.objects.all()
        innt = PassportData.objects.all()
        
        for i in innt:
            iins=str(i.iin)
            if iins == user.username:
                personal=Employee.objects.get(id=i.employee_id)
                entry = Employee.objects.get(pk=i.employee_id)
              
      
            
        if request.method == "POST":
            entry = Employee.objects.get(pk='firstkay')
            queryimeag = request.POST.get('Photo')  
           
            
            cheese_imeag = Employee.objects.get(imeag = queryimeag)
            entry.imeag = cheese_imeag
            entry.save()
        summr = get_summ_alerts(request)
        summs = get_summ_applications()
        context = {"summr": summr, "summs": summs,"user": user, "personal":personal}
        return render(request,"students/home/personalaccounts.html", context )
    
@login_required
@user_passes_test(is_member)
def KSTUeditemployeeaccounts(request, id):
        personal = Employee.objects.get(id=id)
        summr = get_summ_alerts(request)
        summs = get_summ_applications()
        context = {"summr": summr, "summs": summs,"personal":personal}
        
        if request.method == "GET":

            return render(request,"students/home/editpersonalaccounts.html", context )

        return render(request,"students/home/editpersonalaccounts.html", context )
        # return render(request,"students/home/personalaccount.html", context={"user": user}) 

 


@login_required
@user_passes_test(is_member)  
def KSTUeditstud(request):
    inn = get_inn_user(request)
    summr = get_summ_alerts(request)
    summs = get_summ_applications()
    context = {"summr": summr, "summs": summs, "inn": inn}
    return render("students/edit/editstud.html", context)

@login_required
@user_passes_test(is_member) 
def KSTUeditstuds(request, id):
    if request.method == "GET":
        student = Student.objects.get(id=id)
        return render(request, "students/edit/editstuds.html", {"student":student})
    return render(request,"students/edit/editstuds.html")


@login_required
@user_passes_test(is_member)
def KSTUeditstuds(request, id):
    if request.method == "GET":
        student = Student.objects.get(id=id)
        return render(request, "students/edit/editstuds.html", {"student": student})
    return render(request,"students/edit/editstuds.html")

@login_required
@user_passes_test(is_member)
def DataAdded(request):
    inn = get_inn_user(request)
    summr = get_summ_alerts(request)
    summs = get_summ_applications()
    context = {"summr": summr, "summs": summs, "inn": inn}
    return render("students/notification/dataaddedstud.html", context)



@login_required
@user_passes_test(is_member)
def createStudent(request):
    if request.method == "GET":
        form = UploadFileForm(request.POST, request.FILES)
        obj1 = Countryes.objects.all()
        summr = get_summ_alerts(request)
        summs = get_summ_applications()
        context = {"summr": summr, "summs": summs,'form':form, 'countryes':obj1}
        return render(request, 'students/edit/addstudent.html', context )
  
    if request.method == "POST":
      
        queryfirstname = request.POST.get('first_name')
        querysurname = request.POST.get('surname')
        querylastname = request.POST.get('patronymic')
        querydataofbirth = request.POST.get('DateofBirth')
        querynumber_phone = request.POST.get('number_phones')
        querygender = request.POST.get('checkbox')
        qnationality = request.POST.get('nationality')
        queryimeag = request.FILES["file"]
        queryemail = request.POST.get('email')
        Student.objects.create(first_name=queryfirstname, surname = querysurname,last_name=querylastname, data_of_birth = querydataofbirth,number_phone=querynumber_phone, nationality = qnationality, gender=querygender, imeag=queryimeag,email = queryemail)
        
       
        obj = Student.objects.latest('id')
        qtypedoc=request.POST.get('typedoc')
        queryserial = request.POST.get('pserial')
        queryiin = request.POST.get('personalNoinn')
        querynumber = request.POST.get('passportNo')
        queryissuedby = request.POST.get('IssuingAuthority')
        querydateofissue = request.POST.get('DateOfIssue')
        querydateend = request.POST.get('EndDate')
        qdocument = request.POST.get('DocPasport')
        PassportDataS.objects.create(student=obj,typedoc=qtypedoc, inn = queryiin, number=querynumber,  issued_by=queryissuedby, date_of_issue=querydateofissue,date_end=querydateend, serial=queryserial, document=qdocument)
        passwords1=request.POST.get('passportNo')
        passwords= "KSTU" + passwords1 + str(randint(100, 999))
        User.objects.create_user(username=queryiin,
                                 first_name=queryfirstname,
                                 last_name=querysurname,
                                 pname= querylastname,
                                 photolee = queryimeag,
                                 email=queryemail,
                                 password=passwords)
        
        objv = Employee.objects.latest('id')
        from apps_logic.account.models import Passwords
        un = objv.unique_code_user
        Passwords.objects.create(user=User, unique = un, password = passwords)
        subject=str('Ваш логин и пароль для авторизации на сайте SGP.KSTU.KG')
        massage=str("Логин:  " + queryiin + "   Пароль:   " + querynumber)
        send_email(login=queryiin,passw=passwords, useremail=queryemail)
        
     
        
         
         
        #Языки
        querystatelanguage=request.POST.get('019')
        querylanguagesem=request.POST.get('020')
        querylevellang=request.POST.get('021')
        if querylanguagesem != "":
            LanguageProficiencyStudent.objects.create(student=obj,statelanguage=querystatelanguage,languagesem=querylanguagesem,levellang=querylevellang)
       
            v=0
            for v in range(1, 15): 
          
              querylanguagesem= request.POST.get('020vvv'+ str(v))
              testing=None
              if querylanguagesem != testing:
                querylanguagesem=request.POST.get('020vvv'+ str(v))
                querylevellang=request.POST.get('021vvv'+ str(v))
                LanguageProficiencyStudent.objects.create(student=obj,statelanguage=querystatelanguage,languagesem=querylanguagesem,levellang=querylevellang)
       

       
        #Сведения о семейном положении
        queryname_fam= request.POST.get('family')
        querysurname = request.POST.get('surname') 
        queryfirst_name = request.POST.get('name')
        querylast_name = request.POST.get('patronymic')
        queryd_o_b = request.POST.get('dateofb')
        #Сведения о семейном положении
        
        if queryname_fam != "":
            FamilyMembers.objects.create(student = obj, name_fam = queryname_fam , surname = querysurname ,first_name=queryfirst_name,last_name=querylast_name, d_o_b = queryd_o_b )
            i=0
            for i in range(1, 15): 
          
              queryname_fam= request.POST.get('family'+ str(i))
              testing=None
              
              if queryname_fam != testing:
                queryname_fam= request.POST.get('family'+ str(i))
                querysurname = request.POST.get('surname'+str(i)) 
                queryfirst_name = request.POST.get('name'+str(i))
                querylast_name = request.POST.get('patronymic'+str(i))
                queryd_o_b = request.POST.get('dateofb'+str(i))
                FamilyMembers.objects.create(student = obj, name_fam = queryname_fam , surname = querysurname ,first_name=queryfirst_name,last_name=querylast_name, d_o_b = queryd_o_b )
            
       
        #Место рождения
        querycountry = request.POST.get('country')
        queryregion= request.POST.get('Area')
        queryvillage = request.POST.get('village')
        querycitya = request.POST.get('City')
        querydistrict = request.POST.get('district')
        querystreet= request.POST.get('street')
        
        PlaceOfBirth.objects.create( student=obj, country=querycountry, street=querystreet, region=queryregion,village=queryvillage,city= querycitya,district=querydistrict )
        
        
        #Образование сотрудника
       
        type_of_document = request.POST.get('054')
        serial = request.POST.get('011')
        issued_by = request.POST.get('014')
        date_of_issue = request.POST.get('013')
        documents = request.POST.get('015') 
        Education.objects.create( student = obj,type_of_document = type_of_document, serial = serial, issued_by = issued_by, date_of_issue = date_of_issue, documents = documents)
        
        
        return redirect('dataaddedstud')
    
    return render(request, 'students/edit/addstudent.html')


def name(request):
    obj = Employee.objects.all()
    return render(request, 'students/saial.html', {"obj":obj})





def createStudentLeaflet(request, id=None):
    error = ''
    if request.method == "GET":
        try:
            if id:
                obj = Student.objects.get(id=id)
                obj1 = Countryes.objects.all()
            else:
                obj = Student.objects.latest('id')

            summr = get_summ_alerts(request)
            summs = get_summ_applications()
            context = {"summr": summr, "summs": summs,'student':obj,'countryes':obj1}
            return render(request, 'students/edit/studleaflet.html', context )
        except:
                    return redirect('error_404')

    if request.method == "POST":
        obj = Student.objects.get(id=id)
        #Личный листок по учёту кадров
        querydate_elected = request.POST.get('dateoffillng')
        querysignature = request.POST.get('personalsign')
        querynationality = request.POST.get('nationality')
        
        
        #Место рождения
        querycountry = request.POST.get('country')
        queryregion= request.POST.get('Area')
        queryvillage = request.POST.get('village')
        querycitya = request.POST.get('City')
        querydistrict = request.POST.get('district')
        querystreet= request.POST.get('street')
        
        

        #Сведения о семейном положении
        queryname_fam= request.POST.get('family')
        querysurname = request.POST.get('surname') 
        queryfirst_name = request.POST.get('name')
        querylast_name = request.POST.get('patronymic')
        queryd_o_b = request.POST.get('dateofb')
       
        
        #Образование сотрудника
        
        querytitle = request.POST.get('001')
        querydate_enter = request.POST.get('014')
        querydate_close = request.POST.get('015')
        querychoices_learn = request.POST.get('013')
        querydiploma_specialty = request.POST.get('017') #в маделе было какую специальность получил в результате окончания учебного заведеия исправить модель
        queryqualification_of_diploma = request.POST.get('017') #в маделе было какую специальность получил в результате окончания учебного заведеия исправить модель
        querydiploma_number = request.POST.get('018')
       
        #трудовая делятельность/стаж
        queryprofessional_experience = request.POST.get('024')
        querygeneral_experience = request.POST.get('025')
        queryexperience_state_service = request.POST.get('026')
        queryexperience_private_structures = request.POST.get('027')
        querycontinuous_experience = request.POST.get('028')
        querythems = request.POST.get('029')
        querydate_with = request.POST.get('030')
        querydate_end = request.POST.get('031')
        querytype_of_boost = request.POST.get('032')
        querytype_of_document = request.POST.get('033')
        querydocument = request.POST.get('034')
        
        
        #сontinuous_experience проблема
        
        #Языки
        querystatelanguage=request.POST.get('019')
        querylanguagesem=request.POST.get('020')
        querylevellang=request.POST.get('021')
       
       
        #Ученая степень/звание
        
        querystepscience=request.POST.get('022')
        queryrankscience=request.POST.get('023')
        
        
    
    
    
        
        
        #занимаемая должность с начала трудовой деятельности
        queryposition = request.POST.get('035')  #Занимаемая должность
        querystate = request.POST.get('036')#Штат
        queryorganization=request.POST.get('0036')#Наименование организации
        querynum_order = request.POST.get('038')#Начало работы
        querydate_order = request.POST.get('037')#началы работы Номер приказа
        querydeadline = request.POST.get('039')#Окончание работы
        queryend_order = request.POST.get('040')#окончания работы номер приказа
        
        

        #Научные труды
        querythem = request.POST.get('042')#Названия 
        querytype = request.POST.get('043')#Научные труды
        querydate_published = request.POST.get('044')#Дата 
        querydocument = request.POST.get('045')#Подтверждающий документ
        
       
        
        
        #Дипломатический ранг или иные классные звания
        querynamerank = request.POST.get('046')#Названия
        queryrank = request.POST.get('047')# Звания
        querydate_rank = request.POST.get('048')#Дата
        querydocumentrank = request.POST.get('049')#Подтверждающий документ
        
        
        
        
        #Государственные награды
        querynameawards = request.POST.get('050')#Награда
        queryawards = request.POST.get('051')#Названия
        querydate_awards = request.POST.get('052')#Дата  
        querydocumentawards = request.POST.get('053')#Подтвеждающий документ
       
        
        
        #Прибываение заграницей
        # form = BorderForm(request.POST)
        # if form.is_valid():
        #     cd = form.cleaned_data
        #     nameborder = cd.get("nameborder")
        #     border = cd.get('border')
        #     date_border = cd.get("date_border")
        #     date_border_end = cd.get("date_border_end")
        #     BorderEmployee.objects.create( employee = obj, nameborder=nameborder,border=border,date_border=date_border,date_border_end=date_border_end)
        nameborder = request.POST.get("54")
        border = request.POST.get('55')
        date_border = request.POST.get("56")
        date_border_end = request.POST.get("57")
        
  
        
     
       

        #Участье в международных, государственнных и других выборах органах
        querylocationsorgans = request.POST.get('058')#Местонохождени органа
        querynameorgans = request.POST.get('059')#Названия органа
        queryelectedname = request.POST.get('060')#В качестве кого Избран
        querydate_elected1 = request.POST.get('061')#месяц и год Избрания
        querydate_elected_end = request.POST.get('062')#месяц и год Выбытия
        
        
       

        #Воинский учёт сотрудника
        querymilitary_rank = request.POST.get('063')
        querytype_of_army = request.POST.get('064')
        queryright_military = request.POST.get('065')
        queryname_of_place_military = request.POST.get('066')
        querycomposition = request.POST.get('067')
        querybyc = request.POST.get('068')
        
        
        
        
        #Медосмотр
        querydate_passing = request.POST.get('069')#Дата прохождения
        queryplace_of_birth = request.POST.get('070')#Место прохождения
        queryphoto = request.POST.get('071')#Флюорография
       
        
        
        
        #Отпуск
        querytype_holiday = request.POST.get('072')#Вид отпуска
        queryperiod_what = request.POST.get('073')#За какой период: Начало
        queryperiod_end = request.POST.get('074')#Конец
        querystart_date = request.POST.get('075')#Отпуск Начало
        queryend_date = request.POST.get('076')#Отпуск Конец
        querycount_day = request.POST.get('077')#кол дней
        queryorder_number = request.POST.get('078')#приказ
        queryorder_date = request.POST.get('079')#Дата приказа
        querynotuspaydays = request.POST.get('081')#Не использованные дни оплаты
        queryvacation_date = request.POST.get('082')#Отозвать с отпуска с(Дата)
        queryunipaid_days = request.POST.get('083')#Не оплаченные дни
        queryrevoke_order_number = request.POST.get('084')#№ Приказа
        queryrevoke_order_date = request.POST.get('085')#Дата не оплаченные дни 
        
        
        
       
        #сохранение
        #  Личный листок по учёту кадров
        PersonalLeaflet.objects.create( employee=obj, date_elected=querydate_elected, signature=querysignature, nationality=querynationality)
        
        #  Место рождения
        PlaceOfBirth1.objects.create( employee=obj, country=querycountry, street=querystreet, region=queryregion,village=queryvillage,city= querycitya,district=querydistrict )
        
        #Сведения о семейном положении
        
        if queryname_fam != "":
            FamilyMembers.objects.create(employee = obj, name_fam = queryname_fam , surname = querysurname ,first_name=queryfirst_name,last_name=querylast_name, d_o_b = queryd_o_b )
            i=0
            for i in range(1, 15): 
          
              queryname_fam= request.POST.get('family'+ str(i))
              testing=None
             
              if queryname_fam != testing:
                queryname_fam= request.POST.get('family'+ str(i))
                querysurname = request.POST.get('surname'+str(i)) 
                queryfirst_name = request.POST.get('name'+str(i))
                querylast_name = request.POST.get('patronymic'+str(i))
                queryd_o_b = request.POST.get('dateofb'+str(i))
                FamilyMembers.objects.create(employee = obj, name_fam = queryname_fam , surname = querysurname ,first_name=queryfirst_name,last_name=querylast_name, d_o_b = queryd_o_b )
            
        #  Образование сотрудника
        if querytitle != "":
            Education.objects.create( employee = obj,title = querytitle, date_enter = querydate_enter, date_close = querydate_close, choices_learn = querychoices_learn, diploma_specialty = querydiploma_specialty, qualification_of_diploma = queryqualification_of_diploma, diploma_number = querydiploma_number )
        
        #Трудовая делятельность/стаж
        if querydate_end != "":
            ProfessionalDevelopment.objects.create( employee = obj,date_with = querydate_with, date_end = querydate_end, type_of_boost = querytype_of_boost, type_of_document = querytype_of_document, document = querydocument, thems=querythems,professional_experience=queryprofessional_experience, general_experience=querygeneral_experience,experience_state_service=queryexperience_state_service, experience_private_structures=queryexperience_private_structures, сontinuous_experience=queryсontinuous_experience)
        
            w=0
            for w in range(1, 15): 
          
              querythems= request.POST.get('029www'+ str(w))
              testing=None
              if querythems != testing:
                querythems = request.POST.get('029www'+ str(w))
                querydate_with = request.POST.get('030www'+ str(w))
                querydate_end = request.POST.get('031www'+ str(w))
                querytype_of_boost = request.POST.get('032www'+ str(w))
                querytype_of_document = request.POST.get('033www'+ str(w))
                querydocument = request.POST.get('034www'+ str(w))
                ProfessionalDevelopment.objects.create( employee = obj,date_with = querydate_with, date_end = querydate_end, type_of_boost = querytype_of_boost, type_of_document = querytype_of_document, document = querydocument, thems=querythems,professional_experience=queryprofessional_experience, general_experience=querygeneral_experience,experience_state_service=queryexperience_state_service, experience_private_structures=queryexperience_private_structures, сontinuous_experience=queryсontinuous_experience)
        
        
        #  Занимаемая должность с начала трудовой деятельности
        if queryorganization != "":
            Positionwork.objects.create(employee=obj, organization= queryorganization, position = queryposition, state=querystate, num_order=querynum_order,date_order=querydate_order, deadline=querydeadline,end_order=queryend_order)
            g=0
            for g in range(1, 15): 
          
              queryorganization = request.POST.get('035ggg'+ str(g))
              testing=None
              if queryorganization != testing:
                queryposition = request.POST.get('035ggg'+ str(g))  #Занимаемая должность
                querystate = request.POST.get('036ggg'+ str(g))#Штат
                queryorganization=request.POST.get('0036ggg'+ str(g))#Наименование организации
                querynum_order = request.POST.get('038ggg'+ str(g))#Начало работы
                querydate_order = request.POST.get('037ggg'+ str(g))#началы работы Номер приказа
                querydeadline = request.POST.get('039ggg'+ str(g))#Окончание работы
                queryend_order = request.POST.get('040ggg'+ str(g))#окончания работы номер приказа
                Positionwork.objects.create(employee=obj, organization= queryorganization, position = queryposition, state=querystate, num_order=querynum_order,date_order=querydate_order, deadline=querydeadline,end_order=queryend_order)
            
        #Знание языков
        if querylanguagesem != "":
            LanguageProficiencyEmployee.objects.create(employee=obj,statelanguage=querystatelanguage,languagesem=querylanguagesem,levellang=querylevellang)
       
            v=0
            for v in range(1, 15): 
          
              querylanguagesem= request.POST.get('020vvv'+ str(v))
              testing=None
              if querylanguagesem != testing:
                querylanguagesem=request.POST.get('020vvv'+ str(v))
                querylevellang=request.POST.get('021vvv'+ str(v))
                LanguageProficiencyEmployee.objects.create(employee=obj,statelanguage=querystatelanguage,languagesem=querylanguagesem,levellang=querylevellang)
       
       
        #Ученая степень/звание
        if querystepscience != "":
            ScienceDegreeEmployee(stepscience=querystepscience,rankscience=queryrankscience)
            l=0
            for l in range(1, 15): 
          
                querylanguagesem= request.POST.get('020lll'+ str(l))
                testing=None
                if querylanguagesem != testing:
                    querylanguagesem=request.POST.get('020lll'+ str(l))
                    querylevellang=request.POST.get('021lll'+ str(l))
                    ScienceDegreeEmployee(stepscience=querystepscience,rankscience=queryrankscience)
       
        
        #  Научные труды
        if querythem != "":
            ScientificWork.objects.create( employee = obj,document=querydocument,date_published=querydate_published, type=querytype,them=querythem )
            s=0
            for s in range(1, 15): 
          
              querythem= request.POST.get('042sss'+ str(s))
              testing=None
              if querythem != testing:
                querythem = request.POST.get('042sss'+ str(s))#Названия 
                querytype = request.POST.get('043sss'+ str(s))#Научные труды
                querydate_published = request.POST.get('044sss'+ str(s))#Дата 
                querydocument = request.POST.get('045sss'+ str(s))#Подтверждающий документ
                ScientificWork.objects.create( employee = obj,document=querydocument,date_published=querydate_published, type=querytype,them=querythem )
            
       
        
        #  Дипломатический ранг или иные классные звания
        if querynamerank != "":
            RankEmployee.objects.create( employee = obj,namerank=querynamerank,date_rank=querydate_rank, rank=queryrank,documentrank=querydocumentrank)
            r=0
            for r in range(1, 15): 
          
              querynamerank= request.POST.get('046rrr'+ str(r))
              testing=None
              if querynamerank != testing:
                querynamerank = request.POST.get('046rrr'+ str(r))#Названия
                queryrank = request.POST.get('047rrr'+ str(r))# Звания
                querydate_rank = request.POST.get('048rrr'+ str(r))#Дата
                querydocumentrank = request.POST.get('049rrr'+ str(r))#Подтверждающий документ
                RankEmployee.objects.create( employee = obj,namerank=querynamerank,date_rank=querydate_rank, rank=queryrank,documentrank=querydocumentrank)
            
        
        #  Государственные награды
        if querynameawards != "":
            AwardsEmployee.objects.create( employee = obj, nameawards= querynameawards,date_awards=querydate_awards,awards=queryawards, documentawards=querydocumentawards)
            p=0
            for p in range(1, 15): 
          
              querynameawards= request.POST.get('050ppp'+ str(p))
              testing =None
              if querynameawards != testing:
                    querynameawards = request.POST.get('050ppp'+ str(p))#Награда
                    queryawards = request.POST.get('051ppp'+ str(p))#Названия
                    querydate_awards = request.POST.get('052ppp'+ str(p))#Дата  
                    querydocumentawards = request.POST.get('053ppp'+ str(p))#Подтвеждающий документ
                    AwardsEmployee.objects.create( employee = obj, nameawards= querynameawards,date_awards=querydate_awards,awards=queryawards, documentawards=querydocumentawards)
            
        
        #  Прибываение заграницей
       
        if border != "":
            BorderEmployee.objects.create( employee = obj, nameborder=nameborder,border=border,date_border=date_border,date_border_end=date_border_end)
            b=0
            for b in range(1, 15): 
          
              nameborder= request.POST.get('054bbb'+ str(b))
              testing=None
              if nameborder != testing:
                    nameborder = request.POST.get('54bbb'+ str(b))
                    border = request.POST.get('55bbb'+ str(b))
                    date_border = request.POST.get('56bbb'+ str(b))
                    date_border_end = request.POST.get('57bbb'+ str(b))
                    BorderEmployee.objects.create( employee = obj, nameborder=nameborder,border=border,date_border=date_border,date_border_end=date_border_end)
            
        
        
        #  Участье в международных, государственнных и других выборах органах
        if querynameorgans != "":
            ElectionsEmployee.objects.create( employee = obj, locationsorgans=querylocationsorgans,nameorgans=querynameorgans,electedname=queryelectedname,date_elected=querydate_elected1,date_elected_end=querydate_elected_end)
            o=0
            for o in range(1, 15): 
          
              querynameorgans= request.POST.get('059ooo'+ str(o))
              testing=None
              if querynameorgans != testing:
                querylocationsorgans = request.POST.get('058ooo'+ str(o))#Местонохождени органа
                querynameorgans = request.POST.get('059ooo'+ str(o))#Названия органа
                queryelectedname = request.POST.get('060ooo'+ str(o))#В качестве кого Избран
                querydate_elected1 = request.POST.get('061ooo'+ str(o))#месяц и год Избрания
                querydate_elected_end = request.POST.get('062ooo'+ str(o))#месяц и год Выбытия
                ElectionsEmployee.objects.create( employee = obj, locationsorgans=querylocationsorgans,nameorgans=querynameorgans,electedname=queryelectedname,date_elected=querydate_elected1,date_elected_end=querydate_elected_end)
            
        
        #  Воинский учёт сотрудника
        if querymilitary_rank != "":
            MilitaryRegistration.objects.create( employee = obj, military_rank = querymilitary_rank, type_of_army = querytype_of_army, right_military = queryright_military, name_of_place_military = queryname_of_place_military, composition = querycomposition, byc = querybyc )
        
        
        #Медосмотр
        if querydate_passing != "":
            Medical.objects.create( employee = obj,date_passing=querydate_passing,place_of_birth=queryplace_of_birth,photo=queryphoto )
            m=0
            for m in range(1, 15): 
          
              querydate_passing= request.POST.get('069mmm'+ str(m))
              testing=None
              if querydate_passing != testing:
                querydate_passing = request.POST.get('069mmm'+ str(m))#Дата прохождения
                queryplace_of_birth = request.POST.get('070mmm'+ str(m))#Место прохождения
                queryphoto = request.POST.get('071mmm'+ str(m))#Флюорография
                Medical.objects.create( employee = obj,date_passing=querydate_passing,place_of_birth=queryplace_of_birth,photo=queryphoto )
            
        
        #  Отпуск
        if querytype_holiday != "":
            Holiday.objects.create( employee = obj,type_holiday=querytype_holiday,period_what=queryperiod_what,period_end=queryperiod_end ,start_date=querystart_date,end_date=queryend_date,count_day =querycount_day,order_number=queryorder_number,order_date=queryorder_date,notuspaydays=querynotuspaydays,vacation_date=queryvacation_date, unipaid_days=queryunipaid_days,revoke_order_number=queryrevoke_order_number,revoke_order_date=queryrevoke_order_date )
            h=0
            for h in range(1, 15): 
          
              querytype_holiday= request.POST.get('072hhh'+ str(h))
              testing=None
              if querytype_holiday != testing:
                querytype_holiday = request.POST.get('072hhh'+ str(h))#Вид отпуска
                queryperiod_what = request.POST.get('073hhh'+ str(h))#За какой период: Начало
                queryperiod_end = request.POST.get('074hhh'+ str(h))#Конец
                querystart_date = request.POST.get('075hhh'+ str(h))#Отпуск Начало
                queryend_date = request.POST.get('076hhh'+ str(h))#Отпуск Конец
                querycount_day = request.POST.get('077hhh'+ str(h))#кол дней
                queryorder_number = request.POST.get('078hhh'+ str(h))#приказ
                queryorder_date = request.POST.get('079hhh'+ str(h))#Дата приказа
                querynotuspaydays = request.POST.get('081hhh'+ str(h))#Не использованные дни оплаты
                queryvacation_date = request.POST.get('082hhh'+ str(h))#Отозвать с отпуска с(Дата)
                queryunipaid_days = request.POST.get('083hhh'+ str(h))#Не оплаченные дни
                queryrevoke_order_number = request.POST.get('084hhh'+ str(h))#№ Приказа
                queryrevoke_order_date = request.POST.get('085hhh'+ str(h))#Дата не оплаченные дни 
                Holiday.objects.create( employee = obj,type_holiday=querytype_holiday,period_what=queryperiod_what,period_end=queryperiod_end ,start_date=querystart_date,end_date=queryend_date,count_day =querycount_day,order_number=queryorder_number,order_date=queryorder_date,notuspaydays=querynotuspaydays,vacation_date=queryvacation_date, unipaid_days=queryunipaid_days,revoke_order_number=queryrevoke_order_number,revoke_order_date=queryrevoke_order_date )
            
        
        
        
        return redirect('dataadded')
    return render(request, 'students/edit/studleaflet.html')






class SearchSData(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'students/search/studentleafletsearch.html'
    context_object_name = 'results'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['direction'] = Student.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        queryset = queryset.filter(Q(first_name__icontains=q) | Q(surname__icontains=q) | Q(last_name__icontains=q))
        return queryset


def KSTUspd(request):
    inn = get_inn_user(request)
    summr = get_summ_alerts(request)
    summs = get_summ_applications()
    context = {"summr": summr, "summs": summs, "inn": inn}
    return render(request, "students/edit/student_personal_data.html", context)

def KSTUspl(request):
    inn = get_inn_user(request)
    summr = get_summ_alerts(request)
    summs = get_summ_applications()
    context = {"summr": summr, "summs": summs, "inn": inn}
    return render(request, "students/edit/studentpersonalleaflet.html", context)

def KSTUsadd(request):
    inn = get_inn_user(request)
    summr = get_summ_alerts(request)
    summs = get_summ_applications()
    context = {"summr": summr, "summs": summs, "inn": inn}
    return render(request, "students/edit/studentsadd.html", context)


