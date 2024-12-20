from django import forms 
from . import models


attrs = {'class':'form-control'}
class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category','title','description']
        widgets = {
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs)
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = ['category','title','Status']
        widgets = {
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'Status':forms.Select(attrs=attrs)
        }