from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
from datetime import datetime


from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count





def validate(request):
    if request.is_anonymous:
        print(request)
        return False
    elif request:
        print(request)
        return True
    

############### VISTAS #####################

def index(request):
    #duplicates =  Profesional_salud.objects.values('rut_profesional').annotate(count=Count('rut_profesional')).filter(count__gt=1)
    #print(duplicates)
    if request.user.is_authenticated == True:
        user_type = str(request.user.id_tipo_user)
    else:
        user_type = str(request.user)
    print(user_type)
    return render(request, 'app/index.html',{"user_type":user_type} )



@user_passes_test(validate)
def vocalizacion(request):
    #DESCOMENTAR ESTO ES PARA OBTENER LOS DATOS DEL PACIENTE, PARAMETROS Y MOSTRAR EN EL FRONT SE NECESITA EL ID PARA BUSCAR
    # # obj = Parametros.objects.get()
    # # pac = Paciente.objects.get()
    # # {"parametros":obj,"paciente":pac}
    user_type = str(request.user.id_tipo_user)
    return render(request, 'app/vocalizacion.html',{"user_type":user_type})    


@user_passes_test(validate)
def intensidad(request):
    user_type = str(request.user.id_tipo_user)
    return render(request, 'app/intensidad.html',{"user_type":user_type})

############### INTENSIDAD #####################


class IntensidadView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'app/intensidad.html')


# ############### MEDIDOR DECIBEL #####################


# def medidor(request):
#     return render(request, 'app/medidor-sonido.html')

# ############### oscilograma ####################


# ############### EJERCICIO PALABRAS#####################


# def eva_param_func(request):
#     def get(self, request, *args, **kwargs):
#         print(request.user.id)
#         return render(request, 'app/eva_param_func.html')

#     def post(self, request, *args, **kwargs):
#         print("hola estoy en el post")
#     return render(request, 'app/eva_param_func.html')

# ################## EJERCICIO LECTURA#######################


# def eva_param_text(request):
#     return render(request, 'app/eva_param_text.html')

# ################## CRUCIGRAMA########################


# def crucigrama(request):
#     return render(request, 'app/crucigrama.html')

# ###################### MEMORICE #######################


# def memorama(request):
#     data = {
#         'form': MemoriceForm,
#     }
#     if request.method == 'POST':
#         formulario = MemoriceForm(data=request.POST)
#         if formulario.is_valid():
#             post = formulario.save(commit=False)
#             post.acierto = request.POST["acierto"]
#             post.tiempo = request.POST["tiempo"]
#             post.movimientos = request.POST["movimientos"]
#             post.usuario_id = request.user.id
#             formulario.save()
#         else:
#             formulario = MemoriceForm()
#     return render(request, 'app/memorama.html', data)
#     # return render(request, 'app/memorama.html')



def registro(request):
    dato = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        print("re")
        formulario = CustomUserCreationForm(data=request.POST)
        print(formulario.data)
        if formulario.is_valid():
            formulario.save()
            print("registro")
            # user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            # login(request, user)
            messages.success(request,"te has registrado correctamente")
        return redirect('login')
    return render(request, 'registration/registro.html', dato)


# ###################### PreRegistro #######################
@csrf_exempt
def preregistro(request):
    
    if request.method == 'POST':
        print("ssss")
        form = PreRegistroFrom(data=request.POST)
        
        if form.is_valid():
            print("ss3ss")
            rut = form.cleaned_data['rut']
            tipouser = form.cleaned_data['tipo_user']
            form.save()
            print(tipouser)
            if tipouser == 'FonoAudiologo':
                obj = Fonoaudilogos.objects.get(rut=rut)
                obj.preregistrado = 1
                obj.save()
            else:
                form.save()
            return render(request, 'app/preregistro.html', {"form":form})
        else:
            print(form.errors)
    else:
        print("ss32221ss")
        form = PreRegistroFrom()
        return render(request, 'app/preregistro.html', {"form":form})
        
    if request.method == 'GET':
        form = PreRegistroFrom()
        return render(request, 'app/preregistro.html', {"form":form})
 
 
 
    
@csrf_exempt    
def preregistrados(request):
    
    
    data = PreRegistro.objects.all()
    
    
    if request.method == 'POST':
        
        formulario = CustomUserCreationForm(request.POST)
        print("post")
        if formulario.is_valid():
            formulario.save()
            formulario.clean()
            print("sqave")
            return render(request, 'app/preregistrados.html', {"data":data,'form': CustomUserCreationForm()})
        else:
            print(formulario.errors)
            # user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password1"])
            # login(request, user)
        formulario.clean()
        return render(request, 'app/preregistrados.html', {"data":data,'form': CustomUserCreationForm()})
        
        
    if request.method == 'GET':
        print("registro1")
        form = PreRegistroFrom()


  
    
    return render(request, 'app/preregistrados.html', {"data":data,'form': CustomUserCreationForm()})
    
    
    
       
    
    
    
@csrf_exempt
def buscar_rut(request, *args, **kwargs):
    if request.method == 'POST':
        rutFono = request.POST.get('rut')
        print(rutFono)
        objetos = Fonoaudilogos.objects.filter(rut=rutFono).filter(preregistrado=0)
        obj = Fonoaudilogos.objects.filter(rut=rutFono)
        print(obj.count())
        print(objetos.count())
        if objetos.count() == 1:
            datos = Fonoaudilogos.objects.get(rut=rutFono)
            # tipoUser = TipoUsuario.objects.get(nombre_tipo_usuario="Paciente")
            fono = {'Nombre': datos.NombreCompleto, 'rut': datos.rut}
            return JsonResponse(fono)
        elif objetos.count() == 0 and obj.count() == 0:
            pre = PreRegistro.objects.filter(rut=rutFono)
            if pre.count() == 1:
                fono = {'STOP':'STOP'}
                print("YA ESTA PREREGISTRADO")
                return JsonResponse(fono) 
            else:
                fono = {'SI':'SI'}
                print("SIN REGISTRO EN BD")
                return JsonResponse(fono)


        elif objetos.count() == 0:
            print("FONOAUDILOGO PREREGISTRADO")
            fono = {'NO':'NO'}
            return JsonResponse(fono)
        








# ###################### LOGICA PARA GUARDAR AUDIO #######################
@csrf_exempt
def save_audio(request, *args, **kwargs):

    if request.method == 'POST':
        #generamos token para evitar que se sobre escriba MODIFICAR
        print(request.user.username)
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M.%S")
        hms = now.strftime("%H:%M.%S")
        token = get_random_string(length=2)
        nombre = request.POST.get('string')
        archivo = f"{token}_{hms}_{nombre}.mp3"
        audio_file = request.FILES.get('file')
        #Guarda el archivo
        arc = default_storage.save(archivo,audio_file)
        
        document = Audio.objects.create(url_audio=arc,timestamp=current_time,idusuario=request.user)
        document.save()
        return HttpResponse("200")


    return render(request, 'app/vocalizacion.html')

########################## VOCALIZACION ################################
############## CONFIGURAR CORRECTAMENTE PARA GUARDAR#####################










class VocalizacionView(View):
    def post(self, request):
        return render(request, 'app/vocalizacion.html')
    
    
    
    
    
    
    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        print("HOLA")
        return render(request, 'app/login.html')

    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            formulario = CustomUserCreationForm(data=request.POST)
            print(formulario)
            if formulario.is_valid():
                print("postttt")
                user = authenticate(username = formulario.cleaned_data["username"], password= formulario.cleaned_data["password"])
                login(request, user)
                messages.success(request,"te has registrado correctamente")
                return redirect(to='app/index.html')
        return render(request, 'app/login.html')

