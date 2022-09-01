from django.shortcuts import render, HttpResponse, redirect
from PracticeApp.models import Signo
from PracticeApp.forms.forms import FormularioX

# Create your views here.
def home(request):
    #holis="Khe onda?"
    #return HttpResponse(holis)
    contexto={
        'key1':'Vos sabés que ésto es difícil',
        'key2':'Sobre todo para mí.',
        'key3':['esto','es','una','lista'],
    }
    return render(request,'PracticeApp/home.html',contexto)

def formulario_x(request):
    if request.method=='POST':
        formulario1=FormularioX(request.POST)
        print(formulario1)
        if formulario1.is_valid:
            data=formulario1.cleaned_data
            tabla=Signo(nombre=data['nombre'],signo=data['signo'])
            tabla.save()
            #return HttpResponse("Se ha agregado el registro con éxito")    #DEBUG
            return redirect('PracticeAppFormularioX')
    else:
        formulario1=FormularioX()
    return render(request,'PracticeApp/formulario.html',{'signos':formulario1})
