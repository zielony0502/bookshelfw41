from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('add_movie/', views.AddMovieView.as_view(), name='dodaj_film'),
    path('add_director/', views.AddDirectorView.as_view(), name='dodaj_rezysera'),
    path('delete_director/<int:pk>/', views.DeleteDirectorView.as_view(), name='usun_rezysera'),
    path('update_director/<int:pk>/', views.UpdateDirectorView.as_view(), name='edytuj_rezysera')
]
