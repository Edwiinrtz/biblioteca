from django.urls import path

from . import views

urlpatterns = [
    #search material
    path('', views.index, name='index'),
    #add material
    path('add', views.registrar_material),
    #add user
    path('addUser', views.registrar_usuario),
    #add eliminar usuario
    path('deleteUser', views.eliminar_usuario),
    #add prestamo
    path('addPrestamo', views.prestamo),
    #add devolucion
    path('addDevol', views.devolucion),
    #add Material
    path('addMaterial', views.add_material),
    #Historial
    path('historial', views.ver_historial),

    path('material_by_id', views.buscar_material_por_id),

    
]