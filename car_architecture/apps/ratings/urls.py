from django.urls import path
from apps.ratings.views import index, salir, home
from . import views

urlpatterns = [
    path('gestion/', index, name='index'),
    path('salir/', salir, name='salir'),
    path('', home, name='home'),
    path('process_file/', views.process_file, name='process_file'),
    path('scraping/', views.scraping_view, name='scraping'),
]
