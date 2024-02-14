from django import forms
from .models import Zapatilla

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Zapatilla
        fields = ["imagen", "modelo", "marca"]
