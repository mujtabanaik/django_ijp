from django.forms import ModelForm, DateInput
from .models import JobRequirement, JobApplicant


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class JobRequirementForm(BaseForm):
    class Meta:
        model = JobRequirement
        fields = "__all__"
        widgets = {
            'date_posted': DateInput(attrs={'type': 'date'}),
            'date_expiry': DateInput(attrs={'type': 'date'})
        }


class JobApplicantForm(BaseForm):
    class Meta:
        model = JobApplicant
        fields = "__all__"
        exclude = ('status',)
        widgets = {
            'date_applied': DateInput(attrs={'type': 'date'})
        }
