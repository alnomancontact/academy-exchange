from django import forms
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    university_id = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'university_id', 'password1', 'password2']



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'description': forms.Textarea(attrs={'class': 'border rounded p-2 w-full'}),
            'category': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'price': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full', 'step': '0.01'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))
