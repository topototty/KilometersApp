from django.contrib import admin
from django.urls import path, include
from KilometersApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KilometersApp.routing')),
]