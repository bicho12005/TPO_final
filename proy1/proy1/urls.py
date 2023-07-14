"""
URL configuration for proy1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Index
from .views import Galeria
from .views import Servicios
from .views import Contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('galeria/', Galeria.as_view(), name='galeria'),
    path('servicios/', Servicios.as_view(), name='servicios'),
    path('contacto/', Contacto.as_view(), name='contacto'),
]
