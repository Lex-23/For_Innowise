from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee
from rest_framework.filters import OrderingFilter, SearchFilter


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['specialisation']

    ordering_fields = ['country', 'specialisation']
    ordering = ['country', 'specialisation', 'id']


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ['position']
    search = ['position']
    ordering_fields = ['position', 'company']
    ordering = ['position', 'company', 'id']



