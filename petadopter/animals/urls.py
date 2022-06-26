from django import views
from django.conf import settings
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('cats/',views.cats,name='cats'),
    path('dogs/',views.dogs,name='dogs'),
    path('birds/',views.birds,name='birds'),
    path('animal/<int:animal_id>/',views.detail,name="detail"),
    path('success',views.success,name="success"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
