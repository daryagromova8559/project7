from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version

words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'





class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name in words:
            raise ValidationError('Возникла ошибка в Наименовании')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        if description in words:
            raise ValidationError('Возникла ошибка в Описании')
        return description

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
