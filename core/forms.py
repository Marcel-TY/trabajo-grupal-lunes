from django import forms
from .models import Docente, Ramo, Informe


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'especialidad']
        widgets = {
            'nombre':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Matemáticas'}),
        }
        labels = {
            'nombre':       'Nombre',
            'especialidad': 'Especialidad',
        }


class RamoForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Álgebra'}),
        }
        labels = {
            'descripcion': 'Descripción',
        }


class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['docente', 'ramo', 'nom_alu', 'nota_final', 'estado']
        widgets = {
            'docente':    forms.Select(attrs={'class': 'form-select'}),
            'ramo':       forms.Select(attrs={'class': 'form-select'}),
            'nom_alu':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del alumno'}),
            'nota_final': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '1.0', 'max': '7.0'}),
            'estado':     forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'docente':    'Docente',
            'ramo':       'Ramo',
            'nom_alu':    'Nombre del Alumno',
            'nota_final': 'Nota Final',
            'estado':     'Estado',
        }
