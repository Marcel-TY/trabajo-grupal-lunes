from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Docente, Ramo, Informe
from .forms import DocenteForm, RamoForm, InformeForm


def index(request):
    return render(request, 'core/index.html')


# ─────────────────────────── Docente ───────────────────────────

def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'core/docente_list.html', {'docentes': docentes})


def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente creado correctamente.')
            return redirect('docente_list')
    else:
        form = DocenteForm()
    return render(request, 'core/docente_form.html', {'form': form, 'titulo': 'Nuevo Docente'})


def docente_update(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docente actualizado correctamente.')
            return redirect('docente_list')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'core/docente_form.html', {'form': form, 'titulo': 'Editar Docente'})


def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        messages.success(request, 'Docente eliminado.')
        return redirect('docente_list')
    return render(request, 'core/confirm_delete.html', {
        'objeto': docente, 'tipo': 'Docente', 'cancel_url': reverse('docente_list')
    })


# ─────────────────────────── Ramo ───────────────────────────

def ramo_list(request):
    ramos = Ramo.objects.all()
    return render(request, 'core/ramo_list.html', {'ramos': ramos})


def ramo_create(request):
    if request.method == 'POST':
        form = RamoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ramo creado correctamente.')
            return redirect('ramo_list')
    else:
        form = RamoForm()
    return render(request, 'core/ramo_form.html', {'form': form, 'titulo': 'Nuevo Ramo'})


def ramo_update(request, pk):
    ramo = get_object_or_404(Ramo, pk=pk)
    if request.method == 'POST':
        form = RamoForm(request.POST, instance=ramo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ramo actualizado correctamente.')
            return redirect('ramo_list')
    else:
        form = RamoForm(instance=ramo)
    return render(request, 'core/ramo_form.html', {'form': form, 'titulo': 'Editar Ramo'})


def ramo_delete(request, pk):
    ramo = get_object_or_404(Ramo, pk=pk)
    if request.method == 'POST':
        ramo.delete()
        messages.success(request, 'Ramo eliminado.')
        return redirect('ramo_list')
    return render(request, 'core/confirm_delete.html', {
        'objeto': ramo, 'tipo': 'Ramo', 'cancel_url': reverse('ramo_list')
    })


# ─────────────────────────── Informe ───────────────────────────

def informe_list(request):
    informes = Informe.objects.select_related('docente', 'ramo').all()
    return render(request, 'core/informe_list.html', {'informes': informes})


def informe_create(request):
    if request.method == 'POST':
        form = InformeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informe creado correctamente.')
            return redirect('informe_list')
    else:
        form = InformeForm()
    return render(request, 'core/informe_form.html', {'form': form, 'titulo': 'Nuevo Informe'})


def informe_update(request, pk):
    informe = get_object_or_404(Informe, pk=pk)
    if request.method == 'POST':
        form = InformeForm(request.POST, instance=informe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informe actualizado correctamente.')
            return redirect('informe_list')
    else:
        form = InformeForm(instance=informe)
    return render(request, 'core/informe_form.html', {'form': form, 'titulo': 'Editar Informe'})


def informe_delete(request, pk):
    informe = get_object_or_404(Informe, pk=pk)
    if request.method == 'POST':
        informe.delete()
        messages.success(request, 'Informe eliminado.')
        return redirect('informe_list')
    return render(request, 'core/confirm_delete.html', {
        'objeto': informe, 'tipo': 'Informe', 'cancel_url': reverse('informe_list')
    })
