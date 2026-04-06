from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Docente
    path('docentes/',                    views.docente_list,   name='docente_list'),
    path('docentes/nuevo/',              views.docente_create, name='docente_create'),
    path('docentes/<int:pk>/editar/',    views.docente_update, name='docente_update'),
    path('docentes/<int:pk>/eliminar/',  views.docente_delete, name='docente_delete'),

    # Ramo
    path('ramos/',                    views.ramo_list,   name='ramo_list'),
    path('ramos/nuevo/',              views.ramo_create, name='ramo_create'),
    path('ramos/<int:pk>/editar/',    views.ramo_update, name='ramo_update'),
    path('ramos/<int:pk>/eliminar/',  views.ramo_delete, name='ramo_delete'),

    # Informe
    path('informes/',                    views.informe_list,   name='informe_list'),
    path('informes/nuevo/',              views.informe_create, name='informe_create'),
    path('informes/<int:pk>/editar/',    views.informe_update, name='informe_update'),
    path('informes/<int:pk>/eliminar/',  views.informe_delete, name='informe_delete'),
]
