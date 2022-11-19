from django.contrib import admin
from django.urls import path, include

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:id>/', views.place, name='places'),
    path('tinymce/', include('tinymce.urls')),
]
