from django import forms
from .models import Docente, Ramo, Informe

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'especialidad']
        labels = {
            'nombre': 'Nombre del Docente',
            'especialidad': 'Especialidad',
        }

class RamoForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['descripcion']
        labels = {
            'descripcion': 'Descripción del Ramo',
        }

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['docente', 'ramo', 'nom_alu', 'nota_final', 'estado']
        labels = {
            'docente': 'Docente',
            'ramo': 'Ramo',
            'nom_alu': 'Nombre del Alumno',
            'nota_final': 'Nota Final',
            'estado': 'Estado',
        }
