from django.shortcuts import render
from .serializer import DepartmentSerializer, PersonnelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Department, Personnel
from rest_framework.permissions import IsAdminUser

# ListCreateAPIView: listele ve creat et

# Create your views here.
class DepartmentView(ListCreateAPIView):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()
    permission_classes=[IsAdminUser,]

class PersonnelView(ListCreateAPIView):
    serializer_class=PersonnelSerializer
    queryset=Personnel.objects.all()
    permission_classes=[IsAdminUser]

class Personnal_GPD_View(RetrieveUpdateDestroyAPIView):
    serializer_class=PersonnelSerializer
    queryset=Personal.objects.all()