from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from books import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('dodaj_autora/', views.AddAuthorView.as_view(), name='add_author'),
    path('usun_autora/<int:pk>/', views.DeleteAuthorView.as_view(), name='delete_author'),
    path('zmien_autora/<int:pk>', views.UpdateAuthorView.as_view(), name='update_author'),

    path('dodaj_wydawce/', views.AddPublisherView.as_view(), name='add_publisher'),
    path('usun_wydawce/<int:pk>/', views.DeletePublisher.as_view(), name='delete_publisher'),
]
