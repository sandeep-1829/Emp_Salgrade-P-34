from django.shortcuts import render

# Create your views here.

from app.models import *


def equijoins(request):
    EmpObjects=Emp.objects.select_related('deptno').all()
    d={'EmpObjects':EmpObjects}
    return render(request,'equijoins.html',d)
