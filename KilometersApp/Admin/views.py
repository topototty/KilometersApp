from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin, login_url='home')
def AdminPanel(request):
    return render(request, 'admin/admin_panel.html')

@user_passes_test(is_admin, login_url='home')
def Logs(request):
    return render(request, 'admin/log.html')

@user_passes_test(is_admin, login_url='home')
def Statistic(request):
    return render(request, 'admin/statistic.html')