from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Avg, Q
from .models import Docente, Ramo, Informe
from .forms import DocenteForm, RamoForm, InformeForm

# ============================================
# PORTADA
# ============================================
def portada(request):
    """Página de inicio del sistema"""
    return render(request, 'core/portada.html')

# ============================================
# REGISTRO E INICIO DE SESIÓN
# ============================================
def registro(request):
    """Registro de nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido al sistema.')
            return redirect('portada')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

# ============================================
# CRUD DOCENTES
# ============================================
def docentes_lista(request):
    """Lista de docentes con paginación"""
    docentes = Docente.objects.all().order_by('nombre')
    paginator = Paginator(docentes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/docentes_lista.html', {'page_obj': page_obj})

def docente_crear(request):
    """Crear nuevo docente"""
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente creado exitosamente.')
            return redirect('docentes_lista')
    else:
        form = DocenteForm()
    return render(request, 'core/docente_form.html', {'form': form, 'titulo': 'Crear Docente'})

def docente_editar(request, pk):
    """Editar docente existente"""
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente editado exitosamente.')
            return redirect('docentes_lista')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'core/docente_form.html', {'form': form, 'titulo': 'Editar Docente'})

def docente_eliminar(request, pk):
    """Eliminar docente"""
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        messages.success(request, 'Docente eliminado exitosamente.')
        return redirect('docentes_lista')
    return render(request, 'core/docente_confirm_delete.html', {'object': docente})

# ============================================
# CRUD RAMOS
# ============================================
def ramos_lista(request):
    """Lista de ramos con paginación"""
    ramos = Ramo.objects.all().order_by('descripcion')
    paginator = Paginator(ramos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/ramos_lista.html', {'page_obj': page_obj})

def ramo_crear(request):
    """Crear nuevo ramo"""
    if request.method == 'POST':
        form = RamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ramo creado exitosamente.')
            return redirect('ramos_lista')
    else:
        form = RamoForm()
    return render(request, 'core/ramo_form.html', {'form': form, 'titulo': 'Crear Ramo'})

def ramo_editar(request, pk):
    """Editar ramo existente"""
    ramo = get_object_or_404(Ramo, pk=pk)
    if request.method == 'POST':
        form = RamoForm(request.POST, instance=ramo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ramo editado exitosamente.')
            return redirect('ramos_lista')
    else:
        form = RamoForm(instance=ramo)
    return render(request, 'core/ramo_form.html', {'form': form, 'titulo': 'Editar Ramo'})

def ramo_eliminar(request, pk):
    """Eliminar ramo"""
    ramo = get_object_or_404(Ramo, pk=pk)
    if request.method == 'POST':
        ramo.delete()
        messages.success(request, 'Ramo eliminado exitosamente.')
        return redirect('ramos_lista')
    return render(request, 'core/ramo_confirm_delete.html', {'object': ramo})

# ============================================
# CRUD INFORMES
# ============================================
def informes_lista(request):
    """Lista de informes con paginación"""
    informes = Informe.objects.all().order_by('-folio')
    paginator = Paginator(informes, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/informes_lista.html', {'page_obj': page_obj})

def informe_crear(request):
    """Crear nuevo informe"""
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informe creado exitosamente.')
            return redirect('informes_lista')
    else:
        form = InformeForm()
    return render(request, 'core/informe_form.html', {'form': form, 'titulo': 'Crear Informe'})

def informe_editar(request, pk):
    """Editar informe existente"""
    informe = get_object_or_404(Informe, pk=pk)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informe editado exitosamente.')
            return redirect('informes_lista')
    else:
        form = InformeForm(instance=informe)
    return render(request, 'core/informe_form.html', {'form': form, 'titulo': 'Editar Informe'})

def informe_eliminar(request, pk):
    """Eliminar informe"""
    informe = get_object_or_404(Informe, pk=pk)
    if request.method == 'POST':
        informe.delete()
        messages.success(request, 'Informe eliminado exitosamente.')
        return redirect('informes_lista')
    return render(request, 'core/informe_confirm_delete.html', {'object': informe})

# ============================================
# REPORTES
# ============================================
def reportes(request):
    """Vista de reportes del sistema"""
    # Reporte 1: Ramos con cantidad de alumnos reprobados
    reprobados = Informe.objects.filter(
        estado='RP'
    ).values('ramo__descripcion').annotate(
        total=Count('folio')
    ).order_by('-total')
    
    # Reporte 2: Docente, ramo y promedio de notas
    promedios = Informe.objects.values(
        'docente__nombre', 
        'docente__especialidad',
        'ramo__descripcion'
    ).annotate(
        promedio=Avg('nota_final'),
        cantidad_alumnos=Count('folio')
    ).order_by('docente__nombre')
    
    context = {
        'reprobados': reprobados,
        'promedios': promedios,
    }
    return render(request, 'core/reportes.html', context)
