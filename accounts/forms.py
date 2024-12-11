from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User


attrs = {'class':'form-control'}



class UserLoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm,self).__init__( *args, **kwargs)
    
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs=attrs)
    )

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs=attrs)
    )


    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs=attrs)
    )

    password1= forms.CharField(
        label='Password',
        strip=False,
        widget=forms.TextInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label='Password confirm',
        strip=False,
        widget=forms.TextInput(attrs=attrs)
    )
    
    class Meta(UserCreationForm.Meta):
        fields = ('first_name','last_name','username','email')



class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name' : forms.TextInput(attrs=attrs),
            'last_name' : forms.TextInput(attrs=attrs),
            'email' : forms.TextInput(attrs=attrs)
        }

