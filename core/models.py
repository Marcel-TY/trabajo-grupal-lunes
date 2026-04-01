from django.db import models

class Docente(models.Model):
    cod_doc      = models.AutoField(primary_key=True)
    nombre       = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Ramo(models.Model):
    id_ramo     = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.descripcion

class Informe(models.Model):
    ESTADO_CHOICES = [("AP", "Aprobado"), ("RP", "Reprobado")]
    folio      = models.AutoField(primary_key=True)
    docente    = models.ForeignKey(Docente, on_delete=models.CASCADE)
    ramo       = models.ForeignKey(Ramo, on_delete=models.CASCADE)
    nom_alu    = models.CharField(max_length=100)
    nota_final = models.DecimalField(max_digits=4, decimal_places=1)
    estado     = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    def __str__(self):
        return self.nom_alu
