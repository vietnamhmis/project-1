from django import forms

class registerForm(forms.Form):
   # last_name = forms.CharField(max_length=60)
   # first_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class loginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

