from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.

def employee_list(request):
	context = {'employee_list': Employee.objects.all()}
	return render(request, "employee_register/employee_list.html", context)

def employee_form(request, id=0):
  if request.method == "GET":
      if id == 0:
         form = EmployeeForm()
      else:
         employee = Employee.objects.get(pk=id)
         form = EmployeeForm(instance=employee)  
      return render(request, "employee_register/employee_form.html",{'form': form}) 
  else:
      if id == 0:
          form = EmployeeForm(request.POST)
      else:
          employee = Employee.objects.get(pk=id)
          form = EmployeeForm(request.POST, instance=employee)
      if form.is_valid():
          form.save()
      return redirect('/employee/list')

def employee_delete(request, id):
  employee = Employee.objects.get(pk=id)
  employee.delete()
  return redirect('/employee/list')

# Pie Chart
def pie_chart(request):
    labels = []
    data = []
 
    queryset = Employee.objects.order_by('-emp_code')[:5]
    for employee in queryset:
        labels.append(employee.fullname)
        data.append(employee.emp_code)
 
    return render(request, "employee_register/pie_chart.html", {
        'labels': labels,
        'data': data,
    })

# def pie_chart(request):
#     labels = []
#     data = []
 
#     queryset = Employee.objects.order_by('-econtact')[:5]
#     for city in queryset:
#         labels.append(city.ename)
#         data.append(city.econtact)
 
#     return render(request, 'pie_chart.html', {
#         'labels': labels,
#         'data': data,
#     })
