from django import forms

class AddrForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget = forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )
    city = forms.CharField(
        label='Enter Your City',
        widget = forms.TextInput(
            attrs={
                'placeholder': 'City',
                'class': 'form-control'
            }
        )
    )
    address = forms.CharField(
        label='Enter Your Address',
        widget=forms.Textarea(
            attrs={
                'placeholder':'Address',
                'class':'form-control'
            }
        )
    )