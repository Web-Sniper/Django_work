from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label="",
        widget= forms.PasswordInput(
            attrs= {
                'class' : 'form-control',
                'placeholder': 'Password'
            }
        )
    )


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'First Name'
            }
        )
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    location = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }
        )
    )
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User Name'
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email ID'
            }
        )
    )
    mobile = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'
            }
        )
    )