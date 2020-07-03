from django.forms import ModelForm, DateInput
from .models import Employee


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EmployeeForm(BaseForm):
    class Meta:
        model = Employee
        fields = "__all__"
        exclude = ('emp', )
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
            'joining_date': DateInput(attrs={'type': 'date'})
        }

