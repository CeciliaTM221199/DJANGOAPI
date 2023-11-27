from django import forms
from .models import RegistroU


class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroU
        fields = ['nombre','apellidop','apellidom', 'email', 'contra']
        

class validacionRegistro(forms.ModelForm):
    class Meta:
        model = RegistroU
        fields = ['nombre','apellidop','apellidom', 'email', 'contra']

    def clean_mi_campo(self):
        data = self.cleaned_data['nombre','apellidop','apellidom', 'email', 'contra']
        if not data:
            raise forms.ValidationError("Este campo no puede estar vacío.")
        return data