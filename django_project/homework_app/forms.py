from django import forms
from .models import Product 

class ProductUpdateForm(forms.ModelForm):
    choice_product_to_update = forms.ModelChoiceField(queryset=Product.objects.all())
    class Meta:
        model = Product
        fields = ['title', 'description', 'price'] 
    image = forms.ImageField()

