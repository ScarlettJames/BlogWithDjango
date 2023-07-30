from django import forms

class Styling:
    pwdAttrs = {
        'placeholder': 'Enter Your Password',
        'id': 'passwordOne',
        'class': 'form-control w-25',
        }
    userAttrs = {
        'placeholder': 'Enter Your Username',
        'class': 'form-control w-25',
    }

class Registeration(forms.Form):
    username = forms.CharField(max_length=16,min_length=4,strip=True,required=True, label='Username',
                               widget=forms.TextInput(attrs=Styling.userAttrs))
    password = forms.CharField(max_length=16,min_length=8,required=True,label='Password',
                               widget=forms.PasswordInput(attrs=Styling.pwdAttrs))
    
class Login(forms.Form):
    username = forms.CharField(max_length=16,min_length=4,strip=True,required=True, label='Username',
                               widget=forms.TextInput(attrs=Styling.userAttrs))
    password = forms.CharField(max_length=16,min_length=8,required=True,label='Password',
                               widget=forms.PasswordInput(attrs=Styling.pwdAttrs))