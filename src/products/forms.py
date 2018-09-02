from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='')
    description = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={
                                                            "rows": 15,
                                                            "cols": 80
                                                        }
                                  )
                                )
    price = forms.DecimalField(initial=6.66)
