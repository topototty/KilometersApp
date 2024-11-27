from django.urls import path, include
from KilometersApp.Admin import views

urlpatterns = [
    path('panel/', views.AdminPanel, name="admin_panel"),
    path('logs/', views.Logs, name="log"),
    path('statistic/', views.Statistic, name="statistic"),
]
