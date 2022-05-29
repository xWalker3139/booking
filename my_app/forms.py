from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Desk, Contact, Answer

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'nume':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tau...', 'autocomplete':'off'}),
            'prenume':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prenumele tau...', 'autocomplete':'off'}),
            'mesaj':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Mesaj...', 'autocomplete':'off'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...', 'autocomplete':'off'}),
            'telefon':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Numar de telefon...', 'autocomplete':'off'}),
        }

class DeskForm(forms.ModelForm):
    class Meta:
        model = Desk
        fields = ('user', 'tara', 'oras', 'strada', 'etaj', 'imagine')
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'name':'user', 'value':''}),
            'tara':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tara'}),
            'oras':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Oras'}),
            'strada':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Strada'}),
            'etaj':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Etaj'}),
            'imagine':forms.FileInput(),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'option1':forms.Select(attrs={'class':'form-control'}),
            'option2':forms.Select(attrs={'class':'form-control'}),
            'option3':forms.Select(attrs={'class':'form-control'}),
            'option4':forms.Select(attrs={'class':'form-control'}),
        }