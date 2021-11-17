from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
  
  class Meta:
    model = Employee
    # fields = '__all__'
    fields = ('fullname', 'address', 'emp_code', 'email', 'mobile', 'telephone', 'position');
    labels = {
			'fullname':'Full Name',
			'address':'Address',
			'emp_code':'EMP. Code',
			'email':'Email',
			'mobile':'Mobile No.',
			'telephone':'Telephone No.',
			'position':'Position'
		}
