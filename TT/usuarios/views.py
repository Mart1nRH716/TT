# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,'cuenta/dashboard.html',{'section': 'dashboard'})