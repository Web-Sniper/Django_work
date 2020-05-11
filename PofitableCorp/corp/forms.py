from django import forms

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="",
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your name'
            }
        )
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Email'
            }
        )
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your City'
            }
        )
    )
    mobile = forms.IntegerField(
        label="",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Mobile Number'
            }
        )
    )
    query = forms.CharField(
        label="",
        widget= forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Query'
            }
        )
    )