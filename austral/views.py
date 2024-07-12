from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Auto, Marca
from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def index(request):
    context = {
        'title': 'Austral Rent a Car - Inicio',
    }
    return render(request, 'index.html', context)

def admin2(request):
    context = {
        'title': 'Austral Rent a Car - Administración',
    }
    return render(request, 'html/admin.html', context)

def vehiculos(request):
    context = {
        'title': 'Austral Rent a Car - Vehículos',
    }
    return render(request, 'vehiculos.html', context)

def nosotros(request):
    context = {
        'title': 'Austral Rent a Car - Nosotros',
    }
    return render(request, 'equipo.html', context)

def login(request):
    return render(request, 'login.html')
def menu(request):
    request.session["usuario"] = "barby"
    usuario = request.session["usuario"]
    context = {'usuario': usuario}
    return render(request, 'html/admin.html', context)

def admin(request):
    autos = Auto.objects.all()
    context = {'autos': autos}
    return render(request, 'html/vehiculo.html', context)

def agregar(request):
    if request.method != "POST":
        autos = Auto.objects.all()
        context = {'idauto': autos}
        return render(request, 'html/agregar.html', context)
    else:
        id_auto = request.POST["idAuto"]
        nombre = request.POST["nombre"]
        annio = request.POST["fecha"]
        marca = request.POST["Marca"]
        activo = "1"
    
        obj = Auto.objects.create(id_auto=id_auto,
                                   nombre=nombre,
                                   annio=annio,
                                   marca=marca,
                                   activo=1)
        obj.save()
        context = {'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'html/agregar.html', context)

def encontrar(request, pk):
    context = {}
    try:
        auto = Auto.objects.get(id_auto=pk)
        marcas = Marca.objects.all()  
        context = {'auto': auto, 'marcas': marcas}
        return render(request, 'html/modificar.html', context)
    except Auto.DoesNotExist:
        context = {'mensaje': 'Error, id auto no existe'}
        return render(request, 'html/admin.html', context)

def modificar(request):
    if request.method == "POST":
        idauto = request.POST["idauto"]
        nombre = request.POST["nombre"]
        annio = request.POST["fecha"]
        marca = request.POST["marca"]
        color = request.POST["color"]
        cant_pasajeros = request.POST["cant_pasajeros"]
        activo = "1"

        try:
            auto = Auto.objects.get(id_auto=idauto)
            auto.nombre = nombre
            auto.annio = annio
            auto.marca = marca
            auto.color = color
            auto.cant_pasajeros = cant_pasajeros
            auto.activo = activo
            auto.save()
            autos = Auto.objects.all()
            context = {'mensaje': 'OK, datos actualizados con éxito', 'autos': autos}
            return render(request, 'html/modificar.html', context)
        except Auto.DoesNotExist:
            autos = Auto.objects.all()
            context = {'autos': autos, 'mensaje': 'Error, auto no encontrado'}
            return render(request, 'html/admin.html', context)
    else:
        autos = Auto.objects.all()
        context = {'autos': autos}
        return render(request, 'html/admin.html', context)

def eliminar(request, pk):
    try:
        auto = Auto.objects.get(id_auto=pk)
        auto.delete()
        mensaje = "Ok, Datos eliminados satisfactoriamente"
    except Auto.DoesNotExist:
        mensaje = "Error, id auto no existe"

    autos = Auto.objects.all()
    context = {'autos': autos, 'mensaje': mensaje}
    return render(request, 'html/admin.html', context)

def registrate(request):
    if request.method == "POST":
        # Lógica para manejar el registro (guardar en la base de datos, etc.)
        # Aquí puedes agregar la validación y el manejo de errores necesarios.
        context = {'mensaje': 'Registro exitoso!'}
        return render(request, 'html/registro_exitoso.html', context)
    return render(request, 'html/registrate.html')

def ig_view(request):
    return render(request, 'ig.html')
