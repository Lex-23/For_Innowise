from rest_framework import serializers
from .models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'foundation',
            'country',
            'city',
            'specialisation',
            'partnership',
            'getPartner',
            'description',
            'url'
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'company',
            'company_name',
            'name',
            'position',
            'age',
            'url'
        )
