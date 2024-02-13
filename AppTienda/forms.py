from django import forms

class ProductoForm(forms.Form):
    
    imagen= forms.ImageField(label="imagen")
    modelo= forms.CharField(max_length= 100)
    marca= forms.CharField(max_length= 1000)
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        self.fields['imagen'].widget.attrs.update({'class': 'form-control'})
        self.fields['modelo'].widget.attrs.update({'class': 'form-control'})
        self.fields['marca'].widget.attrs.update({'class': 'form-control'})
        