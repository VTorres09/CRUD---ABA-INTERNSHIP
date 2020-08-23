from rest_framework import viewsets, filters
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('employee_id', 'employee_name', 'employee_birth', 'employee_department')