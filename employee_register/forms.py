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
		}
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fiels['position'](queryset=..., empty_label=None)
        # self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required = False
  
  