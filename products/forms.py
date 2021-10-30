from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, BreweryCategory, StyleCategory, CountryCategory


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        breweries = BreweryCategory.objects.all()
        brewery_friendly_names = [(b.id,
                                  b.get_friendly_name()) for b in breweries]
        styles = StyleCategory.objects.all()
        style_friendly_names = [(s.id,
                                s.get_friendly_name()) for s in styles]
        countries = CountryCategory.objects.all()
        country_friendly_names = [(c.id,
                                  c.get_friendly_name()) for c in countries]

        self.fields['brewery'].choices = brewery_friendly_names
        self.fields['style'].choices = style_friendly_names
        self.fields['country'].choices = country_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
