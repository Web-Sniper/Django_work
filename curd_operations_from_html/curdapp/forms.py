from django import forms

class AddProduct(forms.Form):
    prod_name = forms.CharField(
        label="Enter Product Name",
        widget= forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Product Name'
            }
        )
    )
    prod_id = forms.IntegerField(
        label="Enter Product Id",
        widget = forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )
    prod_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget = forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
    prod_color = forms.CharField(
        label="Enter Product Color",
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder': 'Product Color'
            }
        )
    )
    prod_weight = forms.IntegerField(
        label="Enter Product Weight",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Weight in kg'
            }
        )
    )

class UpdateProduct(forms.Form):
    prod_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )
    prod_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Cost'
            }
        )
    )
class DeleteProduct(forms.Form):
    prod_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product ID'
            }
        )
    )
