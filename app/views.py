from django.shortcuts import render

# Create your views here.

from app.models import *

from django.db.models import Q

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


def selfjoins(request):
    EmpObjects=Emp.objects.select_related('mgr').all()
    EmpObjects=Emp.objects.select_related('mgr').filter(sal__gte=2500)
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    EmpObjects=Emp.objects.select_related('mgr').filter(ename='SCOTT')
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename='BLAKE')
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING',sal__lt=3000)
    EmpObjects=Emp.objects.select_related('mgr').all()
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename__isnull=True)
    EmpObjects=Emp.objects.select_related('mgr').all()
    EmpObjects=Emp.objects.select_related('mgr').filter(job='MANAGER',mgr__ename='KING')
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename='JONES')
    EmpObjects=Emp.objects.select_related('mgr').filter(mgr__ename='JONES',sal__lte=3000)
    EmpObjects=Emp.objects.select_related('mgr').filter(job='SALESMAN')
    EmpObjects=Emp.objects.select_related('mgr').filter(job='ANALYST')
    EmpObjects=Emp.objects.select_related('mgr').all()
    EmpObjects=Emp.objects.select_related('mgr').filter(comm__gt=300)
    EmpObjects=Emp.objects.select_related('mgr').filter(ename='BLAKE')
    EmpObjects=Emp.objects.select_related('mgr').all()
    d={'EmpObjects':EmpObjects}
    return render(request,'selfjoins.html',d)



def emp_deptno_mgr(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='JONES')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='FORD')
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='NEW YORK')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') | Q(mgr__ename='SOCTT'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='CLERK') | Q(mgr__ename='BLAKE'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno=20) | Q(ename='FORD'))
    emd=Emp.objects.select_related('deptno','mgr').filter(job='MANAGER')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING',job='MANAGER')
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024,job='CLERK')
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__month=10,job='SALESMAN')
    emd=Emp.objects.select_related('deptno','mgr').filter(job__startswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='H')
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__day=18)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__gte=300)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='SALES',comm__gte=300)
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='ACCOUNTING') | Q(mgr__ename='CLARK'))
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='SALES') | Q(mgr__ename='BLACK'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno=30)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(deptno=10))
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING',sal__lt=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='ANALYST')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='DALLAS')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='R')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='G')
    emd=Emp.objects.select_related('deptno','mgr').all()

    d={'emd':emd}
    return render(request,'emp_deptno_mgr.html',d)




def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=Salgrade.objects.all()
    # Retrieving the data of employees who belongs to grade 4
    #SO=Salgrade.objects.filter(grade=4)  #[grade 4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    # Retrieving the data of employees who belongs to grade 3,4
    SO=Salgrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.losal,sgo.hisal))

    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)
