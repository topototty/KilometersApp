from django.urls import path, include

from KilometersApp import views

urlpatterns = [
    path('', views.HomeNavigation, name="home"),
    path('auth/', include('KilometersApp.Auth.urls')),
    path('admin_panel/', include('KilometersApp.Admin.urls'))
]
