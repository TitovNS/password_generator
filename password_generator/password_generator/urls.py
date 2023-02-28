from django.conf.urls.static import static
from django.urls import path
from generator import views

from password_generator import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
