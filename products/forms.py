from django import forms

from .models import Product

# class ProductForm(forms.Form):
#     title = forms.CharField()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'content', 'price', 'inventory'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 4:
            raise forms.ValidationError('this is not long enough')
        return title
