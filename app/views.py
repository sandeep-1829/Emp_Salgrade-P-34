from django.shortcuts import render

# Create your views here.

from app.models import *


def equijoins(request):
    EmpObjects=Emp.objects.select_related('deptno').all()
    EmpObjects=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EmpObjects=Emp.objects.select_related('deptno').filter(hiredate__month=10)
    EmpObjects=Emp.objects.select_related('deptno').filter(sal__gte=3000)
    EmpObjects=Emp.objects.select_related('deptno').filter(deptno=10)
    EmpObjects=Emp.objects.select_related('deptno').all()
    EmpObjects=Emp.objects.select_related('deptno').filter(deptno__dname='SALES')
    EmpObjects=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EmpObjects=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EmpObjects=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EmpObjects=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EmpObjects=Emp.objects.select_related('deptno').all()
    EmpObjects=Emp.objects.select_related('deptno').filter(sal__lt=2000)
    EmpObjects=Emp.objects.select_related('deptno').filter(sal=3000)
    EmpObjects=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    d={'EmpObjects':EmpObjects}
    return render(request,'equijoins.html',d)
