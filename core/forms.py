# import the standard Django Forms 
# from built-in library 
from django import forms  
from .models import MyUser

class UserForm(forms.ModelForm):
    conpass = forms.CharField(max_length=255,widget=forms.PasswordInput(attrs = {'required pattern': ".{8,}",'placeholder':"Minimum 8 characters"}),label="Confirm Password")

    class Meta:
        model = MyUser
        fields =  ("email","password","conpass","name")
        labels ={
            'email':('Enter your email'),
            'password':('Password'),
            'name':('Full Name')
        }
        widgets = {
            'email' : forms.EmailInput(attrs={"required pattern": "[^@\s]+@[^@\s]+\.[^@\s]+",'placeholder':"Example@email.com"}),
            'password' : forms.PasswordInput(attrs = {'required pattern': ".{8,}",'placeholder':"Minimum 8 characters"}),
            'name' : forms.TextInput(attrs = {'required':'required'})
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=255,widget=forms.EmailInput(attrs={"required pattern": "[^@\s]+@[^@\s]+\.[^@\s]+",'placeholder':"Example@email.com"}))
    password = forms.CharField(label="Password", max_length=255,widget=forms.PasswordInput(attrs = {'required pattern': ".{8,}",'placeholder':"Minimum 8 characters"}))


