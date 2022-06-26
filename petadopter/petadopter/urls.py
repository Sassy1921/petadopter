
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('animals.urls')),
       #dert b7al hakkak 7it makhasch tkhlt liya m3a dyl animals
    path('authentication/',include('authentication.urls')),

]

