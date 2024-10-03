from django.shortcuts import render,redirect
from django.views.generic import View
from empapp.forms import EmployeeForm
from empapp.models import Employee
from django.contrib import messages

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=EmployeeForm()
        return render(request,"empadd.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_instance=EmployeeForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Employee.objects.create(**data)

            messages.success(request,'created successfully')
            return redirect('emp-list')
        else:
             messages.error(request,'failed to add employee')
             return render(request,"empadd.html",{"form":form_instance})

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emplist.html",{"details":qs})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,'empdetail.html',{'employee':qs})

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        messages.success(request,"deleted successful")
        return redirect("emp-list")

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        emp_obj=Employee.objects.get(id=id)
        emp_dict={
            "name":emp_obj.name,
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "salary":emp_obj.salary,
            "contact":emp_obj.contact,
            "address":emp_obj.address
        }
        form_instance=EmployeeForm(initial=emp_dict)
        return render(request,"empedit.html",{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_instance=EmployeeForm(request.POST)
        id=kwargs.get("pk")
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Employee.objects.filter(id=id).update(**data)
            messages.success(request,"employee details updated")
            return redirect('emp-list')
        else:
             messages.error(request,'employee details not updated')
             return render(request,"empedit.html",{"form":form_instance})

class HomeView(View):
    def get(self,request,*args,**kwargs):

        return render(request,'home.html')




            


