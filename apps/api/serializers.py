from rest_framework import serializers
from django.contrib.auth.models import User
from apps.onoxo.models import *


class salarySerializer(serializers.ModelSerializer):
     
     class Meta:
        model = Salary_Model
        fields = ('year_month', 'oklad')

class EmployeeSerializers(serializers.ModelSerializer):
    userid = serializers.IntegerField(source='user.id', read_only=True)
    phone = serializers.SerializerMethodField()
    employee_sp1 = salarySerializer(many = True, required = False)
    class Meta:
        model = Employee_Model
        # fields = '__all__'
        fields = ('id', 'name', 'phone', 'userid', 'employee_sp1')
        
    def get_phone(self, employee):
        return  "+996" + employee.phone_number
        
  

           
        
        