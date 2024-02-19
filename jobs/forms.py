from django import forms
from jobs.models import Jobs

class Jobform(forms.ModelForm):
    class Meta:
        model=Jobs
        fields=['title','description','vacancy']
        widgets={
            'title':forms.TextInput(attrs={'class':'formcontrol'}),
            'description':forms.Textarea(attrs={'class':'formcontrol'}),
            'vacancy':forms.NumberInput(attrs={'class':'formcontrol'}),
        }