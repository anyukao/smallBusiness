from __future__ import division
from ast import Try
from django.db.models import Q
from django.shortcuts import redirect, render
from .models import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import Response

class EmployeeApiView(APIView):
    serializer_class = EmployeeSerializers
    model = User
    permission_classes = (IsAuthenticated)
    
    def get(self, request):
        user = request.user
        employee = Employee_Model.objects.get(user=user)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)

class EmployeesApiView(APIView):
    serializer_class = EmployeeSerializers
    permission_classes = (IsAuthenticated)
    
    def get(self, request):
        employee = Employee_Model.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return Response(serializer.data)
        
        
class EmployeeIDApiView(APIView):
    serializer_class = EmployeeSerializers
    permission_classes = (IsAuthenticated)
   
    def get(self, request,id):
        user = User.objects.get(id=id)
        employee = Employee_Model.objects.get(user=user)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)
    

class EmployeeIDApi(APIView):
    def post(self, request):
        data = request.data
        id = data["id"]        
        user = User.objects.get(id=id)
        employee = Employee_Model.objects.get(user=user)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)
    
    def patch(self, request):
        
        data = request.data
        id = data["id"]        
        user = User.objects.get(id=id)
        employee = Employee_Model.objects.get(user=user)
        try:
            if  data["name"] == None or data["name"] == "":
                pass
            else:
                employee.name = data["name"]
        except:
            pass
        try:
            employee.phone_number = data["phone_number"]
        except:
            pass
        employee.save()
        employee = Employee_Model.objects.get(user=user)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data)