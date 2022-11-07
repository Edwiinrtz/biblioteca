"""
1. Registrar un material en el catálogo.
2. Registrar una persona.
3. Eliminar una persona. 
4. Registrar un préstamo. 
5. Registrar una devolución. 
6.  Incrementar cantidad registrada de un material en específico.
7. Consultar el historial de la biblioteca.
"""
from django.shortcuts import render,redirect
from datetime import date
from .controller import Controller, Material


# Create your views here.
from django.http import HttpResponse


mensaje = 'Bienvenido!'

def index(request):
    global mensaje

    notify = {
        'mensaje':mensaje,
        'parametros':{
            'id':"notify",
            'style':"display:none;"
        }
    }

    context={'materiales':Controller.get_all_material().order_by('-fecha_registro'),'notificacion':notify}

    return render(request,"biblioteca/index.html", context)



def buscar_material_por_id(request):
    global mensaje
    id_material = request.POST.get('id')

    material= Controller.get_one_material(id_material)
    
    mensaje='material no encontrado'

    if material:
        material = {material}
        context={'materiales':material,'notificacion':{False}}
        return render(request,"biblioteca/index.html", context)

    return redirect(index)
    
    

def registrar_material(request):

    global mensaje

    #id,titulo,fecha_registro,cant_registrada
    id = request.POST.get('id')
    titulo = request.POST.get('titulo')
    fecha_registro = date.today()
    cant = request.POST.get('cant')

    resultado = Controller.registrar_material(id=id,titulo=titulo,fecha=fecha_registro,cant=cant)
    mensaje = resultado['mensaje']
    return redirect(index)

def registrar_usuario(request):
    global mensaje

     #,nombre,cedula,rol
    nombre = request.POST.get('nombre')
    cedula = request.POST.get('cc')
    rol = request.POST.get('rol')

    rs = Controller.registrar_usuario(nombre=nombre,cedula=cedula,rol=rol)

    mensaje = rs['mensaje']
    return redirect(index)

def eliminar_usuario(request):
    global mensaje
    cedula = request.POST.get('cc')

    rs = Controller.eliminar_usuario(cedula)

    mensaje = rs['mensaje']

    return redirect(index)


def prestamo(request):
    global mensaje

     #,nombre,cedula,rol
    id_material = request.POST.get('id_material')
    cedula = request.POST.get('cc')
    cantidad = request.POST.get('cant')

    rs = Controller.prestamo(id=id_material,cc=cedula,cant=cantidad)

    mensaje = rs['mensaje']
    return redirect(index)

def devolucion(request):
    global mensaje

     #,nombre,cedula,rol
    id_material = request.POST.get('id_material')
    cedula = request.POST.get('cc')
    cantidad = request.POST.get('cant')

    rs = Controller.devolucion(id=id_material,cc=cedula,cant=cantidad)

    mensaje = rs['mensaje']
    return redirect(index)


def add_material(request):
    global mensaje
    
    id_material = request.POST.get('id_material')
    cantidad = request.POST.get('cant')
    try:
        cantidad = int(cantidad)
        rs = Controller.incrementar_cantidad(id_material,cantidad)       
        mensaje = rs['mensaje']
    except ValueError:
        print('la cantidad a ingresar debe ser un numero')

    return redirect(index)

def ver_historial(request):
    historial = Controller.ver_historial()


    context={'historial':historial.order_by('-id')}


    return render(request,"biblioteca/historial.html",context)
