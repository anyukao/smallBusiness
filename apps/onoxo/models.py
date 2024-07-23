from django.db import models



class Unit_Model(models.Model):
    name = models.CharField(verbose_name="UNIT",max_length=255, null=True )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"


class Job_Title_Model(models.Model):
    job_title = models.CharField(verbose_name="JOB TITLE",max_length=255, null=True )
    
    def __str__(self):
        return self.job_title
    
    class Meta:
        verbose_name = "Job title"
        verbose_name_plural = "Job titles"

class Employee_Model(models.Model):
    first_name = models.CharField(verbose_name="FIRST NAME",max_length=255, null=True )
    name = models.CharField(verbose_name="NAME",max_length=255, null=True )
    second_name = models.CharField(verbose_name="SECOND NAME",max_length=255, null=True , blank=True)
    job_title = models.ForeignKey(Job_Title_Model, verbose_name="JOB TITLE", on_delete=models.SET_NULL, blank=True, null=True, related_name="employee")
    selery = models.CharField(verbose_name="SELERY",max_length=255, null=True )
    adress = models.CharField(verbose_name="ADDRESSS",max_length=255, null=True )
    phone_number =  models.CharField(verbose_name="PHONE NUMBER",max_length=255, null=True )
    date_of_birth = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employeers"



class Finished_Products_Model(models.Model):
    name =  models.CharField(verbose_name="NAME",max_length=255, null=True )
    unit =  models.ForeignKey(Unit_Model, verbose_name="UNIT", on_delete=models.SET_NULL, blank=True, null=True, related_name="finishedProd")
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    sum =  models.CharField(verbose_name="SUM",max_length=255, null=True )

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Finished product"
        verbose_name_plural = "Finished products"




class Production_Model(models.Model):
    product = models.ForeignKey(Finished_Products_Model, verbose_name="PRODUCT", on_delete=models.SET_NULL, blank=True, null=True)
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee_Model, verbose_name="EMPLOYEE", on_delete=models.SET_NULL, blank=True, null=True, related_name="employee_p")
    def __str__(self):
        return  self.product.name
    
    class Meta:
        verbose_name = "Production"
        verbose_name_plural = "Productions"

class Sale_Of_Products_Model(models.Model):
    product = models.ForeignKey(Finished_Products_Model, verbose_name="PRODUCT", on_delete=models.SET_NULL, blank=True, null=True)
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    sum =  models.CharField(verbose_name="SUM",max_length=255, null=True )
    date =  models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee_Model, verbose_name="EMPLOYEE", on_delete=models.SET_NULL, blank=True, null=True, related_name="employee_sp")

    def __str__(self):
        return self.product.name
    
    class Meta:
        verbose_name = "Sale of product"
        verbose_name_plural = "Sale of products"

class Raw_Material_Model(models.Model):
    name = models.CharField(verbose_name="NAME",max_length=255, null=True )
    unit = models.ForeignKey(Unit_Model, verbose_name="UNIT",on_delete=models.SET_NULL, blank=True, null=True, related_name="raw_mat")
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    sum =  models.CharField(verbose_name="SUM",max_length=255, null=True )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Raw material"
        verbose_name_plural = "Raw materials"

class Inqredients_Model(models.Model):
    product = models.ForeignKey(Finished_Products_Model, verbose_name="PRODUCT", on_delete=models.SET_NULL, blank=True, null=True)
    raw_material = models.ForeignKey(Raw_Material_Model, verbose_name="RAW MATERIAL", on_delete=models.SET_NULL, blank=True, null=True)
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    
    def __str__(self):
        try:
            return self.product.name
        except:
            return ""
    
    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        
class Purchase_Raw_Material_Model(models.Model):
    raw_material = models.ForeignKey(Raw_Material_Model, verbose_name="RAW MATERIAL", on_delete=models.SET_NULL, blank=True, null=True)
    amount =  models.CharField(verbose_name="AMOUNT",max_length=255, null=True )
    sum =  models.CharField(verbose_name="SUM",max_length=255, null=True )
    date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee_Model, verbose_name="EMPLOYEE", on_delete=models.SET_NULL, blank=True, null=True, related_name="employee_pr")
    
    def __str__(self):
        return self.employee.name
    
    class Meta:
        verbose_name = "Purchase Raw Material"
        verbose_name_plural = "Purchase Raw Materials"



class Budget_Model(models.Model):
    budjet_amount =  models.CharField(verbose_name="PERCENT",max_length=255, null=True )
    percent =  models.CharField(verbose_name="PERCENT",max_length=255, null=True )
    bonus =  models.CharField(verbose_name="BONUS",max_length=255, null=True )
    def __str__(self):
        return str(self.budjet_amount)
    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"

class Salary_Model(models.Model):
    year_month =  models.CharField(verbose_name="Year and Month",max_length=255, null=True, blank=True )
    employee = models.ForeignKey(Employee_Model, verbose_name="EMPLOYEE", on_delete=models.SET_NULL, blank=True, null=True, related_name="employee_sp1")
    numberOfParticip_Purchase =  models.CharField(verbose_name="Num Of Participations in Purchase",blank=True,max_length=255, null=True )
    numberOfParticip_Production = models.CharField(verbose_name="Num Of Participations in Production",max_length=255, null=True, blank=True )
    numberOfParticip_Sale = models.CharField(verbose_name="Num Of Participations in Sale",max_length=255, null=True, blank=True  )
    amount = models.IntegerField(verbose_name="Num Of All Participations ", null=True, blank=True  )
    bonus = models.CharField(verbose_name="Бонус",max_length=255, null=True, blank=True  )
    oklad = models.CharField(verbose_name="Оклад",max_length=255, null=True, blank=True  )
    salary = models.CharField(verbose_name="Salary",max_length=255, null=True, blank=True )
    status = models.CharField(verbose_name="Status",max_length=255, null=True, blank=True )
    def __str__(self):
        return str(self.employee)
    
    class Meta:
        verbose_name = "Salary for employee"
        verbose_name_plural = "Salary"

class Error_Log(models.Model):
    error = models.CharField(verbose_name="Error",max_length=255, null=True, blank=True  )


class Credit_Model(models.Model):
        sum = models.IntegerField(verbose_name="sum", null=True )
        dateOfPayment = models.DateField(verbose_name="data of payment",null=True, blank=True )
        percentOfCredit = models.FloatField(verbose_name="percent", null=True, blank=True )
        term = models.FloatField(verbose_name="term", null=True )
        penalties =  models.FloatField(verbose_name="percent", null=True ,  blank=True )
        
        
class CreditForEveryMonth_Model(models.Model):
        credit = models.ForeignKey(Credit_Model, verbose_name="Credit", on_delete=models.CASCADE,  related_name="credit")
        SumForMonth = models.FloatField(verbose_name="sum for month", null=True )
        SumWithPercent = models.FloatField(verbose_name="amount of month", null=True )
        SumRemains =  models.FloatField(verbose_name="Remains of month", null=True )
        percent = models.FloatField(verbose_name="percent", null=True )
        penalties =  models.FloatField(verbose_name="percent", null=True )
        dateOfPayment = models.DateField(verbose_name="data of payment", null=True, blank=True )
        status = models.CharField(verbose_name="Status",max_length=255, null=True, blank=True )
        
        def __str__(self):
            return str(self.credit.sum) + " " + str(self.dateOfPayment)
        class Meta:
            ordering = ['-credit','dateOfPayment',]