from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    #Criado Form
    class Meta:
        model = Produto
        fields = '__all__'
