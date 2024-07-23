from __future__ import division
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student


# from dataclasses import field

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    new_password = serializers.CharField(required=True)


class PinSerializerSTUD(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['pin']


class StudentSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    division = serializers.SerializerMethodField()
    email_person = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = 
        fields = ('id',  'first_name', 'surname', 'email_person', 'imeag', 'position', 'division' , 'number_phone')

    def get_position(self, employees):
      
            mov = None
            position = None

            return position
 
    def get_division(self, employees):
     
            mov = None
            division = None

            return division

class StudentDetailSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    
    division = serializers.SerializerMethodField()
    alert_number = serializers.SerializerMethodField()
    is_head_of = serializers.SerializerMethodField()
    is_mol_of = serializers.SerializerMethodField()
    is_stud = serializers.SerializerMethodField()
    # imeag =  serializers.CharField(source="images", read_only=True)
    imeag = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = (
                    'id',
                    'unique_code_user', 
                    'pin',
                    'first_name',
                    'surname',
                    'last_name',
                    'position',
                    'division',
                    'number_phone',
                    'email',
                    'data_of_birth',
                    'imeag',
                    'alert_number',
                    'user',
                    'is_head_of',
                    'is_mol_of',
                    'status',
                    'is_stud'
                    
                )

    def get_position(self, student):
        # try:
        #     mov = Movement.objects.get(employee=employees)
        #     position = mov.position_id.position_title
        # except:
            mov = None
            position = None

            return position

    def get_division(self, student):
        # try:
        #     mov = Movement.objects.get(employee=employees)
        #     division = mov.divisions.division_name
        # except:
            mov = None
            division = None

            return division
    
    def get_alert_number(self,student):
        try:
            count = Alerts.objects.filter(student_id=student).count()
        except:
            count = None
        return count
    
    def get_is_head_of(self, student):
        # try:
        #     mov = Movement.objects.get(employee=employees)
        #     is_head_of = mov.is_head_of
        # except:
            mov = None
            is_head_of = False

            return is_head_of
    
    def get_is_mol_of(self, student):
        # try:
        #     mov = Movement.objects.get(employee=employees)
        #     is_mol_of = mov.is_mol_of
        # except:
            mov = None
            is_mol_of = False

            return is_mol_of
        
    def get_is_stud(self, student):
        # try:
        #     mov = Movement.objects.get(employee=employees)
        #     is_mol_of = mov.is_mol_of
        # except:
            is_stud = True

            return is_stud
        
    def get_imeag(self, student):
        try: 
            # images = Student.objects.get(student=student)
            imeag = str(student.images.url)
          
        except:
            imeag = None
        
        return imeag

    
class StudentProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('imeag',)


class AlertsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alerts
        fields = '__all__'


