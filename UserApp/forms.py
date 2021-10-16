from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators

from Location.models import *

#class PersonForm(UserCreationForm):

#class PersonForm(UserCreationForm):
#    #username = forms.CharField( label="User Name", widget=forms.TextInput(
#    #    attrs={'placeholder': 'Enter Your User Name'}))
#    
#    first_name = forms.CharField( label="First Name", widget=forms.TextInput(
#        attrs={'placeholder': 'Enter Your User Name'}))
#    last_name = forms.CharField( label="Last Name", widget=forms.TextInput(
#        attrs={'placeholder': 'Enter Your User Name'}))
#    email = forms.CharField( label="Email", widget=forms.EmailInput(
#        attrs={'placeholder': 'Enter Your Email '}))
#    
#    
#    
#    class Meta:
#        model = Person
#        fields = ( 'first_name', 'last_name', 'email', 'phone','country', 'city', 'vanue','address','password1','password2') # You Can Change This order
#        
#        
#        
#    def clean(self):
#        print("your are herererererewrewrwerewr")
#        cleaned_data = super(PersonForm, self).clean()
#        password = cleaned_data.get("password")
#        confirm_password = cleaned_data.get("password2")
#        if password != confirm_password:
#            raise forms.ValidationError(
#                "password and confirm_password does not match"
#        )
#            
#            
#    
#    def clean_email(self):
#        username = self.cleaned_data.get('name')
#        email = self.cleaned_data.get('email')
#        if email and Person.objects.filter(email=email).exclude(name=username).count():
#            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
#        return email
#    
#    
#
#    def clean_name(self): # this name shoud be eques to data base filde
#        username = self.cleaned_data.get('name')
#        email = self.cleaned_data.get('email')
#        if username and Person.objects.filter(name=username).exclude(email=email).count():
#            raise forms.ValidationError('This username is already in use. Please supply a different username.')
#        return username
#        
#        
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#        self.fields['city'].queryset = District.objects.none()
#
#        
#
#        if 'country' in self.data:
#            try:
#                country_id = int(self.data.get('country'))
#                self.fields['city'].queryset = District.objects.filter(country_id=country_id).order_by('name')
#            except (ValueError, TypeError):
#                pass  # invalid input from the client; ignore and fallback to empty City queryset
#        elif self.instance.pk:
#            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
#
#        self.fields['vanue'].queryset = District.objects.none()
#        if 'city' in self.data:
#            try:
#                city_id = int(self.data.get('city'))
#                self.fields['vanue'].queryset = SubDistrict.objects.filter(district_id=city_id).order_by('name')
#            except (ValueError, TypeError):
#                pass  # invalid input from the client; ignore and fallback to empty City queryset
#        elif self.instance.pk:
#            #self.fields['vanue'].queryset = self.instance.country.city.vanue_set.order_by('name')
#            self.fields['vanue'].queryset = self.instance.city.vanue_set.order_by('name')
#
#
#
#class CustomerLoginForm(forms.Form):
#    username = forms.CharField(widget=forms.TextInput())
#    password = forms.CharField(widget=forms.PasswordInput())
#    
#    #email = forms.EmailField( label='Email', widget=forms.EmailInput(
#    #    attrs={'placeholder': 'Enter Your email'}))  
#    #password = forms.CharField( label="Password", widget=forms.PasswordInput(
#    #    attrs={'placeholder': 'Enter Your Password'}))
#    
    
    ############################################################################
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user