from django import forms
from inicio.models import Auto

class CrearAuto(forms.Form):
    modelo = forms.CharField(max_length=20)
    marca = forms.CharField(max_length=20)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    
    
class BuscarAuto(forms.Form):
    modelo = forms.CharField(max_length=20, required=False)
    marca = forms.CharField(max_length=20, required=False)
    
class ModificarAuto(forms.ModelForm):
    
    class Meta:
        model = Auto
        fields = "__all__"