from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.shortcuts import render, redirect
def HomeNavigation(request):
    if request.user.is_authenticated and request.user.groups.filter(name='Admin').exists():
        return redirect('admin_panel')
    return render(request, "index.html")