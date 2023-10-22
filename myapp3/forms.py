from django import forms
import datetime



class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=120)



class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])

class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control',
                                       'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class ImageForm(forms.Form):
    image = forms.ImageField()


class UpdateProduct(forms.Form):
    id_product = forms.IntegerField()
    product_name = forms.CharField(max_length=50)
    quantity = forms.IntegerField(min_value=0)

class AddProduct(forms.Form):
    product_name = forms.CharField(max_length=50)
    product_description = forms.CharField(max_length=300)
    price_product = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = forms.IntegerField(min_value=0)
    images = forms.ImageField()


