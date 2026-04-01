# 🏫 Sistema de Gestión Docente — Colegio
Proyecto Django para gestionar información docente: profesores, ramos e informes de notas.

---

## 👥 División de tareas del grupo

| Tarea | Descripción | Estado |
|-------|-------------|--------|
| ✅ 1. Instalación y configuración | Django instalado, proyecto creado, modelos y BD | **LISTO** |
| 🔲 2. Portada / HTML base | Template de presentación y menú de navegación | Pendiente |
| 🔲 3. Módulo de usuarios | Registro, login y logout | Pendiente |
| 🔲 4. CRUD | Formularios para Docente, Ramo e Informe | Pendiente |
| 🔲 5. Reportes | Listar reprobados, promedio por docente | Pendiente |

---

## ⚙️ Lo que ya está hecho (Parte 1)

### Requisitos
- Python 3.13
- Django 6.0.3

### Instalación
```bash
pip install django
```

### Estructura del proyecto
```
gestion_docente/
├── colegio/          ← configuración principal (settings, urls)
├── core/             ← app principal (modelos, vistas, templates)
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py       ← (por crear)
├── templates/        ← carpeta de HTML
└── manage.py
```

### Base de datos — SQLite (ya configurada)
Archivo generado automáticamente: `db.sqlite3`

### Modelos creados (`core/models.py`)

```python
class Docente(models.Model):
    cod_doc      # clave primaria automática
    nombre       # CharField
    especialidad # CharField

class Ramo(models.Model):
    id_ramo      # clave primaria automática
    descripcion  # CharField

class Informe(models.Model):
    folio        # clave primaria automática
    docente      # ForeignKey → Docente
    ramo         # ForeignKey → Ramo
    nom_alu      # CharField (nombre alumno)
    nota_final   # DecimalField
    estado       # 'AP' = Aprobado / 'RP' = Reprobado
```

### Cómo levantar el servidor
```bash
cd C:\Users\Rodney\gestion_docente
python manage.py runserver
```
Abrir: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin (usuario: admin)

---

## 🔲 Parte 2 — Portada y Templates HTML (pendiente)

### Qué hacer
1. Crear `templates/core/base.html` con menú de navegación
2. Crear `templates/core/portada.html` con presentación del sistema
3. Configurar la vista y URL para la portada

### Archivo `core/views.py` — agregar:
```python
from django.shortcuts import render

def portada(request):
    return render(request, 'core/portada.html')
```

### Archivo `colegio/urls.py` — modificar:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

### Crear `core/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
]
```

---

## 🔲 Parte 3 — Módulo de Usuarios (pendiente)

### Qué hacer
Usar el sistema de autenticación incluido en Django.

### En `colegio/urls.py` agregar:
```python
path('accounts/', include('django.contrib.auth.urls')),
path('registro/', views.registro, name='registro'),
```

### En `settings.py` agregar al final:
```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Vista de registro en `core/views.py`:
```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
```

### Templates necesarios:
- `templates/registration/login.html`
- `templates/registration/registro.html`

---

## 🔲 Parte 4 — CRUD (pendiente)

### Qué hacer
Crear vistas para listar, crear, editar y eliminar para cada entidad.

### Estructura de URLs sugerida:
```
/docentes/           → listar docentes
/docentes/nuevo/     → crear docente
/docentes/editar/1/  → editar docente id=1
/docentes/eliminar/1/→ eliminar docente id=1

/ramos/              → listar ramos
/ramos/nuevo/        → crear ramo
...

/informes/           → listar informes
/informes/nuevo/     → crear informe
...
```

### Crear `core/forms.py`:
```python
from django import forms
from .models import Docente, Ramo, Informe

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'especialidad']

class RamoForm(forms.ModelForm):
    class Meta:
        model = Ramo
        fields = ['descripcion']

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ['docente', 'ramo', 'nom_alu', 'nota_final', 'estado']
```

### Templates necesarios (mostrar 5 registros por fila):
- `templates/core/docentes_lista.html`
- `templates/core/docente_form.html`
- `templates/core/ramos_lista.html`
- `templates/core/ramo_form.html`
- `templates/core/informes_lista.html`
- `templates/core/informe_form.html`

---

## 🔲 Parte 5 — Reportes (pendiente)

### Reporte 1: Ramos con cantidad de reprobados
```python
from django.db.models import Count

def reporte_reprobados(request):
    datos = Informe.objects.filter(estado='RP') \
                .values('ramo__descripcion') \
                .annotate(total=Count('folio')) \
                .order_by('-total')
    return render(request, 'core/reporte_reprobados.html', {'datos': datos})
```

### Reporte 2: Docente, ramo que dicta y promedio de notas
```python
from django.db.models import Avg

def reporte_docentes(request):
    datos = Informe.objects.values(
                'docente__nombre',
                'ramo__descripcion'
            ).annotate(promedio=Avg('nota_final'))
    return render(request, 'core/reporte_docentes.html', {'datos': datos})
```

---

## 📦 Comandos útiles

```bash
# Aplicar cambios en modelos
python manage.py makemigrations
python manage.py migrate

# Crear usuario administrador
python manage.py createsuperuser

# Levantar servidor
python manage.py runserver

# Ver panel admin
http://127.0.0.1:8000/admin
```

---

## 🗂️ Settings importantes (`colegio/settings.py`)
- `INSTALLED_APPS` incluye `'core'`
- `TEMPLATES DIRS` apunta a `BASE_DIR / 'templates'`
- Base de datos: SQLite en `db.sqlite3`
- Idioma: `es-cl` / Zona horaria: `America/Santiago`
