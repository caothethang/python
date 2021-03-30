from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many = True)
    return Response(serializer.data , status = status.HTTP_200_OK)

@api_view(['POST'])
def post(self, request, *args, **kwargs):

    fname = request.POST.get('fullName')
    for instance in Employee.objects.all():
        if instance.fullName == fname:
            print('ddax ton tai')
            return Response(status= status.HTTP_304_NOT_MODIFIED)
    serializer = EmployeeSerializer(data = request.data)
    serializer.save()
    return Response(status = status.HTTP_201_CREATED)