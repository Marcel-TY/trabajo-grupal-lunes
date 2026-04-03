from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('registro/', views.registro, name='registro'),
    
    # CRUD Docentes
    path('docentes/', views.docentes_lista, name='docentes_lista'),
    path('docentes/crear/', views.docente_crear, name='docente_crear'),
    path('docentes/editar/<int:pk>/', views.docente_editar, name='docente_editar'),
    path('docentes/eliminar/<int:pk>/', views.docente_eliminar, name='docente_eliminar'),
    
    # CRUD Ramos
    path('ramos/', views.ramos_lista, name='ramos_lista'),
    path('ramos/crear/', views.ramo_crear, name='ramo_crear'),
    path('ramos/editar/<int:pk>/', views.ramo_editar, name='ramo_editar'),
    path('ramos/eliminar/<int:pk>/', views.ramo_eliminar, name='ramo_eliminar'),
    
    # CRUD Informes
    path('informes/', views.informes_lista, name='informes_lista'),
    path('informes/crear/', views.informe_crear, name='informe_crear'),
    path('informes/editar/<int:pk>/', views.informe_editar, name='informe_editar'),
    path('informes/eliminar/<int:pk>/', views.informe_eliminar, name='informe_eliminar'),
    
    # Reportes
    path('reportes/', views.reportes, name='reportes'),
]
