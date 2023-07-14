#from django.shortcuts import render
#from django.http import HttpResponse
#def saludo(request): #primera vista con funcion
#    return render(request, "index.html")
#def galeria(request):
#    return render(request, "galeria.html")
#def servicios(request):
#    return render(request, "servicios.html")
#def contacto(request):
#    return render(request, "contacto.html")
#def homepage(request):
        #return render_to_response('homepage.html'),
        #context_instance=RequestContext(request))

from django.views.generic import TemplateView

#class LandingPage(TemplateView):
#    template_name = "landing.html"

class Index(TemplateView):
    template_name = "index.html"

class Galeria(TemplateView):
    template_name = "galeria.html"

class Servicios(TemplateView):
    template_name = "servicios.html"

class Contacto(TemplateView):
    template_name = "contacto.html"