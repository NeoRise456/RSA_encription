from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp.forms import TextoForm
from myapp.utils import Criptography
from myapp.utils import ProcesadorDeTexto

import json

# Create your views here.

def procesar_texto(request):
    logic = Criptography()
    logic.get_keys()
    if request.method == 'POST':
        data = json.loads(request.body)
        texto = data.get('texto', '')
        accion = data.get('accion', 'encript')
        
        if accion == 'encript':
            texto_procesado = logic.encript(texto)
        else:
            texto_procesado = logic.decript(texto)

        
        return JsonResponse({'texto_procesado': texto_procesado})

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def rsa_app(request):
    logic = Criptography()
    logic.get_keys()
    return render(request,'index.html',
                    {
                        'p' : logic.p,
                        'q' : logic.q,
                        'n' : logic.n,
                        'e' : logic.e,
                        'd' : logic.d,
                        'input' : "",
                        "output" : ""
                    })