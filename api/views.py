from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView 
from django.views import View
from .models import Encuesta, RegistroU
from .forms import RegistroForm
from django.http import *
from django.contrib import messages 

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect

from .models import RegistroU

from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import RegistroForm

from .models import Product

# views.py
from django.shortcuts import render
from paypalrestsdk import Payment
from django.urls import reverse
from django.http import HttpResponseRedirect

class Variable(APIView):
    template_name="ejemplo1.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Login(APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Index(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Login1(APIView):
    template_name="login1.html"
    def post(self,request):
        return render(request,self.template_name)

class Iconos(APIView):
    template_name="icons.html"
    def post(self,request):
        return render(request,self.template_name)
    
class LoginRegistro(APIView):
    template_name="loginRegistro.html"
    def get(self,request):
        return render(request,self.template_name)

class LoginInicio(APIView):
    template_name="loginInicio.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class InserUser(HttpRequest):
    def registro(request):
        if request.method == 'POST':
            form = RegistroForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                contra = form.cleaned_data['contra']
                messages.success(request, 'El registro se ha creado con éxito.')  # Añade un mensaje de confirmación
            # Redirige a la página de inicio de sesión u otra página que desees
            
            # Envía el correo de bienvenida
                subject = 'Bienvenido a DIPRODEM'
                from_email = 'ceciliatm221199@gmail.com'
                recipient_list = [email]
                contexto = {'email': email, 'contra': contra}
                contenido_correo = render_to_string('email.html', contexto)
                send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

            return redirect('iniciar_sesion')
        
        else:
            form = RegistroForm()
        return render(request, 'iniciar_sesion', {'form': form})

    

def iniciar_sesion(request):
    if request.method == 'POST':
        correo1 = request.POST.get('email')
        contra1 = request.POST.get('contra')
        
        try:
            user = RegistroU.objects.get(email=correo1, contra=contra1)
            request.session['email'] = user.email
    
            return redirect('Index')
        except: 
             messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'loginInicio.html')


def chart_view(request):
    #Gama de colores
    gama1 = Encuesta.objects.filter(gama="Azul-Verde").count()
    gama2 = Encuesta.objects.filter(gama="Azul").count()
    gama3 = Encuesta.objects.filter(gama="Azul-Rosa").count()
    

    return render(request, 'chart.html', context = {
        'gama1': gama1,
        'gama2': gama2,
        'gama3': gama3,
    }
)


 