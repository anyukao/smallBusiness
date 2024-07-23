from __future__ import division
from ast import Try
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required


def mainForm_fun(request):
    return render(request, "mainForm.html")


def unit_fun(request):
    if request.method == "GET":
        obj = Unit_Model.objects.all()
        return render(request, "Unit.html", {"units": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            Unit_Model.objects.create(name=name)
        elif button == "Изменить" or button == "Сохранить":
            ids = request.POST.get("id")
            obj = Unit_Model.objects.get(id=ids)
            obj.name = request.POST.get("name")
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Unit_Model.objects.get(id=ids)
            obj.delete()
        return redirect('Unit')


def unitEdit(request, id):
    if request.method == "GET":
        obj = Unit_Model.objects.get(id=id)
        return render(request, "unitEdit.html", {"units": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            Unit_Model.objects.create(name=name)
        elif button == "Изменить" or button == "Сохранить":
            obj = Unit_Model.objects.get(id=id)
            obj.name = request.POST.get("name")
            obj.save()
        elif button == "Удалить":
            obj = Unit_Model.objects.get(id=id)
            obj.delete()
        return redirect('Unit')


def jobTitlePage_fun(request):
    if request.method == "GET":
        obj = Job_Title_Model.objects.all()
        return render(request, "jobTitlePage.html", {"jobs": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            job_title = request.POST.get("job")
            Job_Title_Model.objects.create(job_title=job_title)
        elif button == "Изменить":
            ids = request.POST.get("id")
            obj = Job_Title_Model.objects.get(id=ids)
            obj.job_title = request.POST.get("job")
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Job_Title_Model.objects.get(id=ids)
            obj.delete()
        return redirect('jobTitlePage')


def jobTitlePageedit(request, id):
    if request.method == "GET":
        obj = Job_Title_Model.objects.get(id=id)
        return render(request, "jobTitlePageedit.html", {"jobs": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            job_title = request.POST.get("job")
            Job_Title_Model.objects.create(job_title=job_title)
        elif button == "Изменить" or button == "Сохранить":
            obj = Job_Title_Model.objects.get(id=id)
            obj.job_title = request.POST.get("job")
            obj.save()
        elif button == "Удалить":
            obj = Job_Title_Model.objects.get(id=id)
            obj.delete()
        return redirect('jobTitlePage')


def employee_fun(request):
    if request.method == "GET":
        obj = Employee_Model.objects.all()
        jobs = Job_Title_Model.objects.all()
        return render(request, "Employee.html", {"employee": obj, "jobs": jobs})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            first_name = request.POST.get("first_name")
            name = request.POST.get("name")
            second_name = request.POST.get("second_name")
            job_titleid = request.POST.get("job_title")
            job_title = Job_Title_Model.objects.get(job_title=job_titleid)
            selery = request.POST.get("selery")
            adress = request.POST.get("adress")
            phone_number = request.POST.get("phone_number")
            date_of_birth = request.POST.get("date_of_birth")
            Employee_Model.objects.create(first_name=first_name, name=name, second_name=second_name, job_title=job_title,
                                          selery=selery, adress=adress, phone_number=phone_number, date_of_birth=date_of_birth)
            employee = Employee_Model.objects.latest("id")
            Salary_Model.objects.create(employee=employee)
        elif button == "Изменить":
            ids = request.POST.get("id")
            obj = Employee_Model.objects.get(id=ids)
            # obj.delete()
            obj.first_name = request.POST.get("first_name")
            obj.name = request.POST.get("name")
            obj.second_name = request.POST.get("second_name")
            job_titleid = request.POST.get("job_title")
            obj.job_title = Job_Title_Model.objects.get(job_title=job_titleid)
            obj.selery = request.POST.get("selery")
            obj.adress = request.POST.get("adress")
            obj.phone_number = request.POST.get("phone_number")
            obj.date_of_birth = request.POST.get("date_of_birth")
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Employee_Model.objects.get(id=ids)
            obj.delete()
        return redirect("Employee")


def employeeedit(request, id):
    if request.method == "GET":
        obj = Employee_Model.objects.get(id=id)
        jobs = Job_Title_Model.objects.all()
        return render(request, "employeeedit.html", {"employee": obj, "jobs": jobs})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            first_name = request.POST.get("first_name")
            name = request.POST.get("name")
            second_name = request.POST.get("second_name")
            job_titleid = request.POST.get("job_title")
            job_title = Job_Title_Model.objects.get(job_title=job_titleid)
            selery = request.POST.get("selery")
            adress = request.POST.get("adress")
            phone_number = request.POST.get("phone_number")
            date_of_birth = request.POST.get("date_of_birth")
            Employee_Model.objects.create(first_name=first_name, name=name, second_name=second_name, job_title=job_title,
                                          selery=selery, adress=adress, phone_number=phone_number, date_of_birth=date_of_birth)
        elif button == "Изменить" or button == "Сохранить":
            obj = Employee_Model.objects.get(id=id)
            obj.first_name = request.POST.get("first_name")
            obj.name = request.POST.get("name")
            obj.second_name = request.POST.get("second_name")
            job_titleid = request.POST.get("job_title")
            if job_titleid == "None" or job_titleid == "":
                pass
            else:
                obj.job_title = Job_Title_Model.objects.get(
                    job_title=job_titleid)
            obj.selery = request.POST.get("selery")
            obj.adress = request.POST.get("adress")
            obj.phone_number = request.POST.get("phone_number")
            lol = request.POST.get("date_of_birth")
            if lol != "":
                obj.date_of_birth = request.POST.get("date_of_birth")
            obj.save()
        elif button == "Удалить":
            obj = Employee_Model.objects.get(id=id)
            obj.delete()
        return redirect("Employee")


def finishedProduct_fun(request):
    if request.method == "GET":
        obj = Finished_Products_Model.objects.all()
        units = Unit_Model.objects.all()
        return render(request, "finishedProduct.html", {"finishedProduct": obj, "units": units})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            Finished_Products_Model.objects.create(
                name=name, unit=unit, amount=amount, sum=sum)
        elif button == "Изменить":
            ids = request.POST.get("id")
            obj = Finished_Products_Model.objects.get(id=ids)
            obj.name = request.POST.get("name")
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Finished_Products_Model.objects.get(id=ids)
            obj.delete()
        return redirect("finishedProduct")


def finishedProductedit(request, id):
    if request.method == "GET":
        obj = Finished_Products_Model.objects.get(id=id)
        units = Unit_Model.objects.all()
        return render(request, "finishedProductedit.html", {"finishedProduct": obj, "units": units})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            Finished_Products_Model.objects.create(
                name=name, unit=unit, amount=amount, sum=sum)
        elif button == "Изменить" or button == "Сохранить":
            obj = Finished_Products_Model.objects.get(id=id)
            obj.name = request.POST.get("name")
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            obj.save()
        elif button == "Удалить":
            obj = Finished_Products_Model.objects.get(id=id)
            obj.delete()
        return redirect("finishedProduct")


def production_fun(request):
    if request.method == "GET":
        finishedProduct = Finished_Products_Model.objects.all()
        employee = Employee_Model.objects.all()
        obj = Production_Model.objects.all()
        return render(request, "production.html", {"production": obj, "finishedProduct": finishedProduct, "employee": employee})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("product")
            product = Finished_Products_Model.objects.get(name=productid)
            amount = request.POST.get("amount")
            date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            employee = Employee_Model.objects.get(name=employeeid)
            alling = Inqredients_Model.objects.filter(product=product)

            check = 0
            for i in alling:
                name = i.raw_material.name
                obj = Raw_Material_Model.objects.get(name=name)
                if float(i.amount)*float(amount) > float(obj.amount):
                    check = 1
            if check == 0:
                summ = 0
                ps = float(product.sum)
                for i in alling:
                    raw_material = i.raw_material
                    amt = float(raw_material.amount)
                    rm = float(raw_material.sum)
                    raw_material.amount = float(
                        raw_material.amount) - float(i.amount) * float(amount)
                    raw_material.sum = (
                            float(raw_material.sum)/float(amt))*raw_material.amount

                    rawm = rm - float(raw_material.sum)
                    summ = summ + rawm
                    print(summ)
                    raw_material.save()

                product.sum = summ+float(ps)
                print(product.sum)
                product.save()

                Production_Model.objects.create(
                    product=product, amount=amount, date=date, employee=employee)
            else:
                error = "Недостаточно сырья"
                finishedProduct = Finished_Products_Model.objects.all()
                employee = Employee_Model.objects.all()
                obj = Production_Model.objects.all()
                return render(request, "production.html", {"production": obj, "finishedProduct": finishedProduct, "employee": employee, "error": error})

            am = product.amount
            product.amount = float(am)+float(amount)
            # sum = float(product.sum)+(float(product.sum)/float(am)*float(amount))
            # product.sum = int(sum)
            product.save()

        elif button == "Изменить":
            idpr = request.POST.get("id")
            obj = Production_Model.objects.get(id=idpr)
            obj.amount = request.POST.get("amount")
            obj.date = request.POST.get("date")
            obj.save()
        elif button == "Удалить":
            idpr = request.POST.get("id")
            obj = Production_Model.objects.get(id=idpr)
            obj.delete()
        return redirect("production")


def productionEdit(request, id):
    if request.method == "GET":
        finishedProduct = Finished_Products_Model.objects.all()
        employee = Employee_Model.objects.all()
        obj = Production_Model.objects.get(id=id)
        return render(request, "productionEdit.html", {"production": obj, "finishedProduct": finishedProduct, "employee": employee})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("product")
            product = Finished_Products_Model.objects.get(name=productid)
            amount = request.POST.get("amount")
            date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            employee = Employee_Model.objects.get(name=employeeid)
            Production_Model.objects.create(
                product=product, amount=amount, date=date, employee=employee)
        elif button == "Изменить" or button == "Сохранить":
            obj = Production_Model.objects.get(id=id)
            obj.amount = request.POST.get("amount")
            lol1 = request.POST.get("date")
            if lol1 != "":
                obj.date = request.POST.get("date")
            obj.save()
        elif button == "Удалить":
            obj = Production_Model.objects.get(id=id)
            obj.delete()
        return redirect("production")


def saleOfProduct_fun(request):
    if request.method == "GET":
        obj = Sale_Of_Products_Model.objects.all()
        productFin = Finished_Products_Model.objects.all()
        employee = Employee_Model.objects.all()
        return render(request, "saleOfProduct.html", {"saleOfProduct": obj, "productFin": productFin, "employee": employee})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("product")
            product = Finished_Products_Model.objects.get(name=productid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            employee = Employee_Model.objects.get(name=employeeid)
            amountt = product.amount
            if product.amount >= amount:
                Sale_Of_Products_Model.objects.create(
                    product=product, amount=amount, sum=sum, date=date, employee=employee)
                prAm = float(product.amount)-float(amount)
                budj1 = Budget_Model.objects.latest("id")
                product.sum = float(product.sum)-float(product.sum) / \
                    float(product.amount)*float(amount)
                product.amount = int(prAm)
                try:
                   bud = float(budj1.budjet_amount)+(float(product.sum) / float(prAm)*float(amount)*(1+(float(budj1.percent)/100)))
                except:
                   bud = 0
                budj1.budjet_amount = bud
                budj1.save()
                product.save()
            else:
                error = "Не хвататет количества данного продукта! Количество:" + \
                    str(amountt)
                obj = Sale_Of_Products_Model.objects.all()
                productFin = Finished_Products_Model.objects.all()
                employee = Employee_Model.objects.all()
                return render(request, "saleOfProduct.html", {"saleOfProduct": obj, "productFin": productFin, "employee": employee, 'error': error})
        elif button == "Изменить":
            ids = request.POST.get("id")
            obj = Sale_Of_Products_Model.objects.get(id=ids)
            productid = request.POST.get("product")
            obj.product = Finished_Products_Model.objects.get(name=productid)
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            employeeid = request.POST.get("employee")
            obj.employee = Employee_Model.objects.get(name=employeeid)
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Sale_Of_Products_Model.objects.get(id=ids)
            obj.delete()
        return redirect("saleOfProduct")


def saleOfProductedit(request, id):
    if request.method == "GET":
        obj = Sale_Of_Products_Model.objects.get(id=id)
        productFin = Finished_Products_Model.objects.all()
        employee = Employee_Model.objects.all()
        return render(request, "saleOfProductedit.html", {"saleOfProduct": obj, "productFin": productFin, "employee": employee})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("product")
            product = Finished_Products_Model.objects.get(name=productid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            employee = Employee_Model.objects.get(name=employeeid)
            Sale_Of_Products_Model.objects.create(
                product=product, amount=amount, sum=sum, date=date, employee=employee)
            amountt = product.amount
            if product.amount >= amount:
                product.amount = int(product.amount)-int(amount)
                budj1 = Budget_Model.objects.latest("id")
                budj1.budjet_amount = int(budj1.budjet_amount)+int(sum)
                budj1.save()
                product.save()
            else:
                error = "Не хвататет количества данного продукта! Количество:" + \
                    str(amountt)
                obj = Sale_Of_Products_Model.objects.all()
                productFin = Finished_Products_Model.objects.all()
                employee = Employee_Model.objects.all()
                obj.delete()
                return render(request, "saleOfProduct.html", {"saleOfProduct": obj, "productFin": productFin, "employee": employee, 'error': error})

        elif button == "Изменить" or button == "Сохранить":
            obj = Sale_Of_Products_Model.objects.get(id=id)
            productid = request.POST.get("product")
            obj.product = Finished_Products_Model.objects.get(name=productid)
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            employeeid = request.POST.get("employee")
            obj.employee = Employee_Model.objects.get(name=employeeid)
            lol1 = request.POST.get("date")
            if lol1 != "":
                obj.date = request.POST.get("date")
            obj.save()

        elif button == "Удалить":
            obj = Sale_Of_Products_Model.objects.get(id=id)
            obj.delete()
        return redirect("saleOfProduct")


def rawMaterials_fun(request):
    if request.method == "GET":
        obj = Raw_Material_Model.objects.all()
        units = Unit_Model.objects.all()
        return render(request, "rawMaterials.html", {"rawMaterials": obj, "units": units})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            Raw_Material_Model.objects.create(
                name=name, unit=unit, amount=amount, sum=sum)
        elif button == "Изменить" or button == "Сохранить":
            ids = request.POST.get("id")
            obj = Raw_Material_Model.objects.get(id=ids)
            obj.name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            obj.save()
        return redirect("rawMaterials")


def rawMaterialsEdit(request, id):
    if request.method == "GET":
        obj = Raw_Material_Model.objects.get(id=id)
        units = Unit_Model.objects.all()
        return render(request, "rawMaterialsEdit.html", {"rawMaterials": obj, "units": units})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            Raw_Material_Model.objects.create(
                name=name, unit=unit, amount=amount, sum=sum)
        elif button == "Изменить" or button == "Сохранить":
            obj = Raw_Material_Model.objects.get(id=id)
            obj.name = request.POST.get("name")
            unitid = request.POST.get("unit")
            unit = Unit_Model.objects.get(name=unitid)
            obj.amount = request.POST.get("amount")
            obj.sum = request.POST.get("sum")
            obj.save()
        elif button == "Удалить":
            obj = Raw_Material_Model.objects.get(id=id)
            obj.delete()
        return redirect("rawMaterials")


def ingredients_fun(request):
    if request.method == "GET":
        finish_prod = Finished_Products_Model.objects.all()
        raw_material = Raw_Material_Model.objects.all()
        obj = Inqredients_Model.objects.all()
        return render(request, "Ingredients.html", {"ingredients": obj, 'finish_prod': finish_prod, 'raw_material': raw_material})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("idprod")
            if productid == "Выберите продукт":
                errors = "Выберите продукт!"
                finish_prod = Finished_Products_Model.objects.all()
                raw_material = Raw_Material_Model.objects.all()
                obj = Inqredients_Model.objects.all()
                return render(request, "Ingredients.html",{"errors":errors,"ingredients": obj, 'finish_prod': finish_prod, 'raw_material': raw_material})
            
            product = Finished_Products_Model.objects.get(name=productid)
            raw_materialid = request.POST.get("raw_material")
            raw_material = Raw_Material_Model.objects.get(name=raw_materialid)
            amount = request.POST.get("amount")
            alling = Inqredients_Model.objects.filter(product=product)
            log = 0
            drugoe = raw_material.amount
            raw_material.amount = float(raw_material.amount)-float(amount)
            lol = float(0)
            if raw_material.amount >= lol:
                for i in alling:
                    if i.raw_material == raw_material:
                        log = 1
                if log == 0:
                    Inqredients_Model.objects.create(
                        product=product, raw_material=raw_material, amount=amount)
                    raw_material.sum = float(
                        raw_material.sum)-(float(amount)*(float(raw_material.sum)/float(drugoe)))
                    raw_material.save()
                    product = Finished_Products_Model.objects.get(
                        name=productid)
                    alling = Inqredients_Model.objects.filter(product=product)
                    mass = []
                    for i in alling:
                        name_row_m = i.raw_material.name
                        row_m = Raw_Material_Model.objects.get(name=name_row_m)
                        summ = float(row_m.sum)/float(row_m.amount)
                        result = float(summ) * float(i.amount)
                        mass.append(result)
                    summ_prod = 0
                    for i in mass:
                        summ_prod = float(summ_prod) + float(i)
                    product.sum = int(summ_prod)*product.amount
                    product.save()

            else:

                error = "Не хвататет запаса данного сырья! Запас данного сырья:" + \
                    str(drugoe)
                product = Finished_Products_Model.objects.get(id=product.id)
                finish_prod = Finished_Products_Model.objects.all()
                raw_material = Raw_Material_Model.objects.all()
                obj = Inqredients_Model.objects.all()
                return render(request, "Ingredientsred.html", {"ingredients": obj, "product": product, 'finish_prod': finish_prod, 'raw_material': raw_material, 'error': error})
        return redirect("Ingredientslog", id=product.id)


def ingredients_funred(request, id):
    if request.method == "GET":
        product = Finished_Products_Model.objects.get(id=id)
        finish_prod = Finished_Products_Model.objects.all()
        raw_material = Raw_Material_Model.objects.all()
        obj = Inqredients_Model.objects.all()
        return render(request, "Ingredientsred.html", {"ingredients": obj, "product": product, 'finish_prod': finish_prod, 'raw_material': raw_material})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            productid = request.POST.get("idprod")
          
            product = Finished_Products_Model.objects.get(name=productid)
            raw_materialid = request.POST.get("raw_material")
            raw_material = Raw_Material_Model.objects.get(name=raw_materialid)
            amount = request.POST.get("amount")
            alling = Inqredients_Model.objects.filter(product=product)
            log = 0
            drugoe = raw_material.amount
            raw_material.amount = float(raw_material.amount)-float(amount)
            lol = float(0)
            if raw_material.amount >= lol:
                for i in alling:
                    if i.raw_material == raw_material:
                        log = 1
                if log == 0:
                    Inqredients_Model.objects.create(
                        product=product, raw_material=raw_material, amount=amount)
                    raw_material.sum = float(
                        raw_material.sum)-(float(amount)*(float(raw_material.sum)/float(drugoe)))
                    raw_material.save()
                    product = Finished_Products_Model.objects.get(
                        name=productid)
                    alling = Inqredients_Model.objects.filter(product=product)
                    mass = []
                    for i in alling:
                        name_row_m = i.raw_material.name
                        row_m = Raw_Material_Model.objects.get(name=name_row_m)
                        summ = float(row_m.sum)/float(row_m.amount)
                        result = float(summ) * float(i.amount)
                        mass.append(result)

                    summ_prod = 0
                    for i in mass:
                        summ_prod = float(summ_prod) + float(i)

                    product.sum = int(summ_prod)
                    product.save()

            else:
                error = "Не хвататет запаса данного сырья! Запас сырья:" + \
                    str(drugoe)
                product = Finished_Products_Model.objects.get(id=id)
                finish_prod = Finished_Products_Model.objects.all()
                raw_material = Raw_Material_Model.objects.all()
                obj = Inqredients_Model.objects.all()
                return render(request, "Ingredientsred.html", {"ingredients": obj, "product": product, 'finish_prod': finish_prod, 'raw_material': raw_material, 'error': error})

        return redirect("Ingredientslog", id=product.id)


def ingredientsedit(request, id):
    if request.method == "GET":
        product = Inqredients_Model.objects.get(id=id)
        finish_prod = Finished_Products_Model.objects.all()
        raw_material = Raw_Material_Model.objects.all()
        obj = Inqredients_Model.objects.get(id=id)
        return render(request, "ingredientsedit.html", {"ingredients": obj, "product": product, 'finish_prod': finish_prod, 'raw_material': raw_material})
    if request.method == "POST":
        button = request.POST.get("updates")
        
        if button == "Создать":
            
            productid = request.POST.get("product")
           
            product = Finished_Products_Model.objects.get(name=productid)
            raw_materialid = request.POST.get("raw_material")
            raw_material = Raw_Material_Model.objects.get(name=raw_materialid)
            amount = request.POST.get("amount")
            Inqredients_Model.objects.create(
                product=product, raw_material=raw_material, amount=amount)
        elif button == "Изменить" or button == "Сохранить":
            obj = Inqredients_Model.objects.get(id=id)
            productid = request.POST.get("idprod")
            product = Finished_Products_Model.objects.get(name=productid)
            raw_materialid = request.POST.get("raw_material")
            obj.raw_material = Raw_Material_Model.objects.get(
                name=raw_materialid)
            obj.amount = request.POST.get("amount")
            obj.save()
            raw_materialid = request.POST.get("raw_material")
            raw_material = Raw_Material_Model.objects.get(name=raw_materialid)
            drugoe = raw_material.amount
            if float(raw_material.amount) > 0:
                raw_material.sum = float(
                    raw_material.sum)-(float(obj.amount)*(float(raw_material.sum)/float(drugoe)))
                raw_material.save()
            else:
                error = "Не хвататет запаса данного сырья! Запас данного сырья:"
                finish_prod = Finished_Products_Model.objects.all()
                raw_material = Raw_Material_Model.objects.all()
                obj = Inqredients_Model.objects.all()
                return render(request, "Ingredientsred.html", {"ingredients": obj, "product": product, 'finish_prod': finish_prod, 'raw_material': raw_material, 'error': error})
        elif button == "Удалить":
            obj = Inqredients_Model.objects.get(id=id)
            productid = request.POST.get("idprod")
            product = Finished_Products_Model.objects.get(name=productid)
            obj.delete()
        return redirect("Ingredientslog", id=product.id)


def purchaseRawM_fun(request):
    if request.method == "GET":
        obj = Purchase_Raw_Material_Model.objects.all()
        employee = Employee_Model.objects.all()
        Raw_material = Raw_Material_Model.objects.all()
        budj = Budget_Model.objects.latest("id")
        return render(request, "purchaseRawM.html", {"purchaseRawM": obj, "employee": employee, "raw_material": Raw_material})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            raw_materialid = request.POST.get("raw_material")
            raw_material = Raw_Material_Model.objects.get(name=raw_materialid)
            amount = request.POST.get("amount")
            sum = request.POST.get("sum")
            budj = Budget_Model.objects.latest("id")
            kek = budj.budjet_amount
            budj.budjet_amount = float(budj.budjet_amount)-float(sum)
            if budj.budjet_amount < 0:
                obj = Purchase_Raw_Material_Model.objects.all()
                employee = Employee_Model.objects.all()
                Raw_material = Raw_Material_Model.objects.all()
                error = "You don't have the budjet! your budjet:" + str(kek)
                return render(request, "purchaseRawM.html", {"purchaseRawM": obj, "employee": employee, "Raw_material": Raw_material, "error": error})
            else:
                raw_material.sum = float(raw_material.sum)+float(sum)
                raw_material.save()
                budj.save()
            date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            employee = Employee_Model.objects.get(name=employeeid)
            # employeei = Employee_Model.objects.all()
            # sm = Salary_Model.objects.all()
            # for i in employeei:
            #     for j in sm:
            #         Purch = Purchase_Raw_Material_Model.objects.filter(
            #                 employee=i)
            #         count = 0
            #         for j in Purch:
            #             if date == sm.year_month:
                        
            Purchase_Raw_Material_Model.objects.create(
                raw_material=raw_material, amount=amount, sum=sum, date=date, employee=employee)
            raw_material.amount = float(raw_material.amount)+float(amount)
            raw_material.save()
        return redirect("purchaseRawM")


def purchaseRawMEdit(request, id):
    if request.method == "GET":
        obj = Purchase_Raw_Material_Model.objects.get(id=id)
        employee = Employee_Model.objects.all()
        Raw_material = Raw_Material_Model.objects.all()
        return render(request, "purchaseRawMEdit.html", {"purchaseRawM": obj, "employee": employee, "Raw_material": Raw_material})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Изменить" or button == "Сохранить":
            obj = Purchase_Raw_Material_Model.objects.get(id=id)
            raw_materialid = request.POST.get("raw_material")
            obj.raw_material = Raw_Material_Model.objects.get(
                name=raw_materialid)
            obj.amount = request.POST.get("amount")
            budj = Budget_Model.objects.latest("id")
            prinSum = request.POST.get("sum")
            if prinSum > obj.sum:
                raznisa = int(prinSum) - int(obj.sum)
                budj.budjet_amount = int(budj.budjet_amount)-int(raznisa)
                budj.save()
            elif prinSum < obj.sum:
                raznisa = int(obj.sum) - int(prinSum)
                budj.budjet_amount = int(budj.budjet_amount)+int(raznisa)
                budj.save()
            obj.sum = request.POST.get("sum")
            lol1 = request.POST.get("date")
            if lol1 != "":
                obj.date = request.POST.get("date")
            employeeid = request.POST.get("employee")
            obj.employee = Employee_Model.objects.get(name=employeeid)
        

            obj.save()
        elif button == "Удалить":
            obj = Purchase_Raw_Material_Model.objects.get(id=id)
            obj.delete()
        return redirect("purchaseRawM")


def budjet_fun(request):
    if request.method == "GET":
        obj = Budget_Model.objects.all()
        return render(request, "budjet.html", {"budget": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            amount = request.POST.get("amount")
            percent = request.POST.get("precent")
            bonus = request.POST.get("bonus")
            Budget_Model.objects.create(
                budjet_amount=amount, percent=percent, bonus=bonus)
        elif button == "Изменить":
            ids = request.POST.get("id")
            obj = Budget_Model.objects.get(id=ids)
            obj.budjet_amount = request.POST.get("amount")
            obj.percent = request.POST.get("precent")
            obj.bonus = request.POST.get("bonus")
            obj.save()
        elif button == "Удалить":
            ids = request.POST.get("id")
            obj = Budget_Model.objects.get(id=ids)
            obj.delete()
        return redirect("budjet")


def budjetEdit(request, id):
    if request.method == "GET":
        obj = Budget_Model.objects.get(id=id)
        return render(request, "budjetEdit.html", {"budget": obj})
    if request.method == "POST":
        button = request.POST.get("updates")
        if button == "Создать":
            amount = request.POST.get("amount")
            percent = request.POST.get("precent")
            bonus = request.POST.get("bonus")
            Budget_Model.objects.create(
                budjet_amount=amount, percent=percent, bonus=bonus)
        elif button == "Изменить" or button == "Сохранить":
            obj = Budget_Model.objects.get(id=id)
            obj.budjet_amount = request.POST.get("amount")
            obj.percent = request.POST.get("precent")
            obj.bonus = request.POST.get("bonus")
            obj.save()
        elif button == "Удалить":
            obj = Budget_Model.objects.get(id=id)
            obj.delete()
        return redirect("budjet")

def SalaryEdit(request, id):
    if request.method == "GET":
        obj = Salary_Model.objects.get(id=id)
        return render(request, "SalaryEdit.html", {"salarry": obj})
    if request.method == "POST":
        status = request.POST.get("status")
        obj = Salary_Model.objects.get(id=id)
        check = str(obj.year_month)
        salary = request.POST.get("salary")
        obj.salary = salary
        obj.save()
        er = Error_Log.objects.latest("id")
        er.error = "-"
        er.save()
        return redirect("salarys", check=check)



def SalaryNext(request, check):
    if request.method == "GET":
        obj = Salary_Model.objects.all()
        employee = Employee_Model.objects.all()
        posts = 0
        for i in employee:
            for j in obj:
                if check == j.year_month:
                    if i == j.employee:
                        posts = 1
                        employee_data = j
            if posts == 1 and employee_data.status != "True":
                
                try:
                    Purch = Purchase_Raw_Material_Model.objects.filter(
                        employee=i)
                    count = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        if check == date:
                            count = count+1
                    employee_data.numberOfParticip_Purchase = str(count)
                except:
                    employee_data.numberOfParticip_Purchase = ""
                    count = 0

                try:
                    Purch = Production_Model.objects.filter(employee=i)
                    count1 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count1 = count1+1
                    employee_data.numberOfParticip_Production = str(count1)
                except:
                    employee_data.numberOfParticip_Production = ""
                    count1 = 0

                try:
                    Purch = Sale_Of_Products_Model.objects.filter(employee=i)
                    count2 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count2 = count2+1
                    employee_data.numberOfParticip_Sale = str(count2)
                except:
                    employee_data.numberOfParticip_Sale = ""
                    count2 = 0
                budj = Budget_Model.objects.latest("id")
                
                employee = Employee_Model.objects.all()
                counts = count+count1+count2
                employee = Employee_Model.objects.all()
                
                try:
                    employee_data.oklad = i.selery
                except:
                    employee_data.oklad = 0
                employee_data.amount = int(count)+int(count1)+int(count2)
                bonus = int(budj.bonus) * employee_data.amount
                employee_data.bonus = bonus
                employee_data.salary = ((int(bonus)*int(i.selery))/100)+int(i.selery)
                employee_data.save()

            if posts == 0:
                try:
                    Purch = Purchase_Raw_Material_Model.objects.filter(
                        employee=i)
                    count = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        if check == date:
                            count = count+1
                    numberOfParticip_Purchase = str(count)
                except:
                    numberOfParticip_Purchase = ""
                    count = 0

                try:
                    Purch = Production_Model.objects.filter(employee=i)
                    count1 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count1 = count1+1
                    numberOfParticip_Production = str(count1)
                except:
                    numberOfParticip_Production = ""
                    count1 = 0

                try:
                    Purch = Sale_Of_Products_Model.objects.filter(employee=i)
                    count2 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count2 = count2+1
                    numberOfParticip_Sale = str(count2)
                except:
                    numberOfParticip_Sale = ""
                    count2 = 0
                budj = Budget_Model.objects.latest("id")
                # bonus = int(budj.bonus)
                employee = Employee_Model.objects.all()
                counts = count+count1+count2
                employee = Employee_Model.objects.all()
                salary = (((counts*bonus)*int(i.selery))/100)+int(i.selery)
                try:
                    oklad = i.selery
                except:
                    oklad = 0
                amount = int(count)+int(count1)+int(count2)
                bonus = int(budj.bonus)*amount
                Salary_Model.objects.create(year_month=check, employee=i, numberOfParticip_Sale=numberOfParticip_Sale, numberOfParticip_Production=numberOfParticip_Production,
                                            numberOfParticip_Purchase=numberOfParticip_Purchase, salary=salary, bonus =bonus, amount = amount, oklad = oklad)

        sets = Salary_Model.objects.filter(year_month=check)
        budj = Budget_Model.objects.latest("id")
        sumbudj = budj.budjet_amount
        per = 0
        for i in sets:
                if i.status == "True":
                    per = 1
        eroorr = Error_Log.objects.latest("id")
        error = eroorr.error
        return render(request, "SalaryNext.html", {"salarry": sets, "year_month": check, "sumbudj":sumbudj, "per":per, "error":error})

    if request.method == "POST":
        err = Error_Log.objects.latest("id")
        err.error = "-"
        err.save()
        
        status = request.POST.get("status")
        if status == "True":
    
            check = request.POST.get("year_month")
            obj = Salary_Model.objects.filter(year_month=check)
            summ = 0
            for i in obj:
                summ = summ + float(i.salary)

            budj = Budget_Model.objects.latest("id")
            if summ < float(budj.budjet_amount):
                budj.budjet_amount = float(budj.budjet_amount) - float(summ)
                for i in obj:
                    i.status = "True"
                    i.save()
                error1 = Error_Log.objects.latest("id")
                error1.error = "Issued"
                error1.save()
                # error = "Выдано"

                budj.save()
            else:
                sum = summ - float(budj.budjet_amount)
                error1 = Error_Log.objects.latest("id")
                error1.error = "Недостаточно бюджета, недостаточно: " + str(sum) + " Сомов"
                error1.save()
                # error = "Недостаточно бюджета, недостаточно: " + str(sum) + " Сомов"
            sets = Salary_Model.objects.filter(year_month=check)
            budj = Budget_Model.objects.latest("id")
            sumbudj = budj.budjet_amount
            per = 0
            for i in sets:
                if i.status == "True":
                    per = 1
            return redirect("salarys",check = check)

        check = request.POST.get("year_month")
        obj = Salary_Model.objects.all()
        employee = Employee_Model.objects.all()
        posts = 0
        for i in employee:
            for j in obj:
                if check == j.year_month:
                    if i == j.employee:
                        posts = 1
                        employee_data = j
                        
            if posts == 1 and employee_data.status != "True":
                
                try:
                    Purch = Purchase_Raw_Material_Model.objects.filter(
                        employee=i)
                    count = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        if check == date:
                            count = count+1
                    employee_data.numberOfParticip_Purchase = str(count)
                except:
                    employee_data.numberOfParticip_Purchase = ""
                    count = 0

                try:
                    Purch = Production_Model.objects.filter(employee=i)
                    count1 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count1 = count1+1
                    employee_data.numberOfParticip_Production = str(count1)
                except:
                    employee_data.numberOfParticip_Production = ""
                    count1 = 0

                try:
                    Purch = Sale_Of_Products_Model.objects.filter(employee=i)
                    count2 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        print(date)
                        if check == date:
                            count2 = count2+1
                    employee_data.numberOfParticip_Sale = str(count2)
                except:
                    employee_data.numberOfParticip_Sale = ""
                    count2 = 0
                budj = Budget_Model.objects.latest("id")
                bonus = int(budj.bonus)
                employee_data.bonus = bonus
                employee = Employee_Model.objects.all()
                counts = count+count1+count2
                employee = Employee_Model.objects.all()
                employee_data.salary = (((counts*bonus)*int(i.selery))/100)+int(i.selery)
                try:
                    employee_data.oklad = i.selery
                except:
                    employee_data.oklad = 0
                employee_data.amount = int(count)+int(count1)+int(count2)
                bonus = int(budj.bonus)*employee_data.amount
                employee_data.bonus = bonus
                employee_data.save()
            if posts == 0:
                try:
                    Purch = Purchase_Raw_Material_Model.objects.filter(
                        employee=i)
                    count = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        if check == date:
                            count = count+1
                    numberOfParticip_Purchase = str(count)
                except:
                    numberOfParticip_Purchase = ""
                    count = 0

                try:
                    Purch = Production_Model.objects.filter(employee=i)
                    count1 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)

                        if check == date:
                            count1 = count1+1
                    numberOfParticip_Production = str(count1)
                except:
                    numberOfParticip_Production = ""
                    count1 = 0

                try:
                    Purch = Sale_Of_Products_Model.objects.filter(employee=i)
                    count2 = 0

                    for j in Purch:
                        date = str(j.date.year) + "-0" + str(j.date.month)
                        if check == date:
                            count2 = count2+1
                    numberOfParticip_Sale = str(count2)
                except:
                    numberOfParticip_Sale = ""
                    count2 = 0
                try:
                    oklad = i.selery
                except:
                    oklad = 0
                budj = Budget_Model.objects.latest("id")
                employee = Employee_Model.objects.all()
                amount = int(count)+int(count1)+int(count2)
                bonus = int(budj.bonus)*amount
                salary = (((amount*int(budj.bonus))* int(i.selery))/100)+int(i.selery)
                Salary_Model.objects.create(year_month=check, employee=i, numberOfParticip_Sale=numberOfParticip_Sale, numberOfParticip_Production=numberOfParticip_Production,
                                            numberOfParticip_Purchase=numberOfParticip_Purchase, salary=salary, amount = amount, oklad=oklad, bonus=bonus)

        sets = Salary_Model.objects.filter(year_month=check)
        budj = Budget_Model.objects.latest("id")
        sumbudj = budj.budjet_amount
        per = 0
        for i in sets:
                if i.status == "True":
                    per = 1
        return redirect("salarys", check = check)
from datetime import datetime, timedelta
def calculate_payment_date(start_date, month_offset):
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    payment_date = start_date + timedelta(days=month_offset * 30)
    return payment_date.strftime("%Y-%m-%d")
from dateutil.relativedelta import relativedelta
from datetime import date
def credit(request):
    if request.method == "GET":
        try:
          obj = Credit_Model.objects.all()
        except:
            obj = ""
        return render(request, "credit.html", {"credit": obj})
    
    if request.method == "POST":
            sum = request.POST.get('sum')
            dateOfPayment = date.today()  
            percentOfCredit = request.POST.get('percent')
            term = request.POST.get('term')
            penalties=request.POST.get("penalties")
            getting = Credit_Model.objects.create(sum=sum, dateOfPayment=dateOfPayment, percentOfCredit=percentOfCredit,term=term, penalties=penalties)
            SumForMonth  = 0
            SumWithPercent = 0 
            penalties = 0
            SumRemains = sum
          
            dateOfPayment = dateOfPayment
            status = "Get"
            remains = CreditForEveryMonth_Model.objects.create(credit=getting,SumRemains=SumRemains, SumForMonth=SumForMonth, SumWithPercent = SumWithPercent,  penalties=penalties, dateOfPayment =dateOfPayment,status=status)
          
            SumForMonth = float(sum)/float(term) #Сколько мы платим за каждый месяц
           
            SumWithPercent = ((float(SumRemains)*float(percentOfCredit))/100)/12 
            SumRemains = float(remains.SumRemains) - float(SumForMonth)
            dateOfPayment = date.today() +  relativedelta(months=1)
            status = False
            remains = CreditForEveryMonth_Model.objects.create(credit=getting,SumRemains=SumRemains, SumForMonth=SumForMonth, SumWithPercent = SumWithPercent,  penalties=penalties, dateOfPayment =dateOfPayment,status=status)
            terms = int(term) - 2 
            for i in range(terms):
                
                SumWithPercent = ((float(SumRemains)*float(percentOfCredit))/100)/12
                SumRemains = float(SumRemains) - float(SumForMonth)
                dateOfPayment = dateOfPayment + relativedelta(months=1)
                status = False
                remains = CreditForEveryMonth_Model.objects.create(credit=getting,SumRemains=SumRemains, SumForMonth=SumForMonth, SumWithPercent = SumWithPercent,  penalties=penalties, dateOfPayment =dateOfPayment,status=status)
            
                
                
                
            return redirect('credit')

def CreditForEveryMonth(request, id):
    if request.method == "GET":
        credit = Credit_Model.objects.get(id=id)
        obj = CreditForEveryMonth_Model.objects.filter(credit=credit)
        fiter_false = obj.filter(status=False)
        first = fiter_false.first()
        if first.dateOfPayment < date.today():
            dateOfpenalties = date.today() - first.dateOfPayment
            days = dateOfpenalties.days
            first.penalties = float(days) * ((first.SumWithPercent+first.SumForMonth)*credit.penalties/100)
            first.save()

        objsave = CreditForEveryMonth_Model.objects.filter(credit=credit)

        return render(request, "CreditForEveryMonth.html", {"credit": objsave})

    if request.method == "POST":
        id_crid = request.POST.get('id')
        obj = CreditForEveryMonth_Model.objects.get(id=id_crid)
        credit = Credit_Model.objects.get(id=obj.credit.id)
        if obj.dateOfPayment < date.today():
            dateOfpenalties = date.today() - obj.dateOfPayment
            days = dateOfpenalties.days
            obj.penalties = float(days)*((float(obj.SumWithPercent)+obj.SumForMonth)*float(credit.penalties)/100)
            obj.dateOfPayment = date.today() 
            obj.status = "True"
            obj.save()
        else:
            obj.dateOfPayment = date.today() 
            obj.status = "True"
            obj.save()
        return redirect('creditik', id=id)
  
