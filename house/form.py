from django import forms
from house.models import House

class HouseModelForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
    
        if price < 60000:
            self.add_error('price', 'Só é possível cadastrar casas com valor acima de R$-60.000')
        else:
            return price
        
    def clean_construction_year(self):
        year_construction = self.cleaned_data.get('year_construction')

        if year_construction < 2000:
            self.add_error('year_construction', 'Só é possível cadastrar casas com o ano de construção cima de 2000')
        else:
            return year_construction