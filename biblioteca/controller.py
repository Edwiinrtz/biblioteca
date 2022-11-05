"""
1. Registrar un material en el catálogo. :LISTO
2. Registrar una persona. :LISTO

3. Eliminar una persona. 

4. Registrar un préstamo.: LISTO 
5. Registrar una devolución. LISTO

6.  Incrementar cantidad registrada de un material en específico. LISTO
7. Consultar el historial de la biblioteca.
"""
from .models import Material,Usuario, Registro

class Controller:

    def validar_existencia(modelo,id):
        try:
            return modelo.objects.get(id=id)
        except:
            return False
    
    def get_all_material():
        return Material.objects.all()

    def get_one_material(id):
        return Controller.validar_existencia(Material,id)
    
        
    def registrar_material(id,titulo,cant,fecha):

        nuevo_material = Material(id,titulo,fecha,cant,cant)

        #validar si el material ya existe en bbdd
        exist = Controller.validar_existencia(Material,nuevo_material.id)

        if(exist):
            return {'status':False,'mensaje':"El material ya existe, no fue registrado"}

        #en caso de que no exista añadir material
        nuevo_material.save()

        return {'status':True,'mensaje':"Registrado con exito"}
    
    def registrar_usuario(nombre,cedula,rol):

        roles_max_cant = {'1':5,'2':3,'3':1}

        nuevo_usuario = Usuario(nombre,cedula,rol,roles_max_cant[rol],0)

        exist = Controller.validar_existencia(Usuario,nuevo_usuario.id)

        if(exist):
            return {'status':False,'mensaje':"El Usuario ya existe, no puede registrarlo de nuevo"}

        #en caso de que no exista añadir material
        nuevo_usuario.save()
        return {'status':True,'mensaje':"Registrado con exito"}

    def eliminar_usuario(cedula):
        #recuperar usuario
        usuario = Controller.validar_existencia(Usuario,cedula)

        if(not usuario):
            print('Usuario no encontrado')
            return False

        if(usuario.prestamos_actuales > 0):
            print('El usuario debe devolver todos los materiales que tenga en su poder')
            return False

        usuario.delete()
        print('Usuario eliminado satisfactoriamente')
        return True


    def prestamo(id,cc,cant:int):

        material = Controller.validar_existencia(Material,id)

        usuario = Controller.validar_existencia(Usuario,cc)
        cant = int(cant)
        if(not material):
            print('Material no encontrado')
            return False

        if(not usuario):
            print('Usuario no encontrado')
            return False

        if(usuario.cant_max < cant or usuario.prestamos_actuales + cant > usuario.cant_max):
            print('El usuario no puede prestar ese cantidad de recursos')
            return False
        
        if(material.cant_actual < cant):
            print('No hay suficiente material')
            return False

        material.cant_actual-= cant
        usuario.prestamos_actuales+= cant

        nuevo_registro = Registro(tipo="Prestamo",material=material.id,usuario=usuario.id,cantidad=cant)

        nuevo_registro.save()
        material.save()
        usuario.save()
        return "Prestamo realizado con exito"


    
    def devolucion(id,cc,cant):

        material = Controller.validar_existencia(Material,id)

        usuario = Controller.validar_existencia(Usuario,cc)
        cant = int(cant)

        if(not material):
            print('Material no encontrado')
            return False

        if(not usuario):
            print('Usuario no encontrado')
            return False

        if(usuario.cant_max < cant):
            print('El usuario no puede tener esa cantidad de libros en su poder')
            return False
        
        if(material.cant_actual + cant > material.cant_registrada):
            print('El usuario está entregando mas materiales de los posibles')
            return False

        material.cant_actual+= cant
        usuario.prestamos_actuales-= cant 

        nuevo_registro = Registro(tipo="Devolucion",material=material.id,usuario=usuario.id,cantidad=cant)

        nuevo_registro.save()
        material.save()
        usuario.save()
        return "Devolucion realizada con exito"

    def incrementar_cantidad(id,cantidad:int):

        material = Controller.validar_existencia(Material,id)

        if(not material):
            print('material no existente')
            return False
        
        material.cant_registrada = material.cant_registrada + cantidad
        material.cant_actual =  material.cant_actual + cantidad

        print("Material registrado con exito")
        material.save()
        return True

    def ver_historial():
        return Registro.objects.all()


