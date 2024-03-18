# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Alumno, Profesor
from .forms import LoginForm, UserRegistrationForm, UserEditForm, AlumnoEditForm

@login_required
def dashboard(request):
    return render(request,'cuenta/dashboard.html',{'section': 'dashboard'})

@login_required
def edit_alumno(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        alumno_form = AlumnoEditForm(instance=request.user.alumno, data=request.POST)
        if user_form.is_valid() and alumno_form.is_valid():
            user_form.save()
            alumno_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        alumno_form = AlumnoEditForm(instance=request.user.alumno)
    return render(request,'cuenta/edit.html',{'user_form': user_form,
                                               'alumno_form': alumno_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
             # Create a new user object but avoid saving it yet
             new_user = user_form.save(commit=False)
             # Set the chosen password
             new_user.set_password(user_form.cleaned_data['password'])
             # Save the User object
             new_user.save()
             Alumno.objects.create(user=new_user)
             return render(request,'cuenta/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'cuenta/register.html',{'user_form': user_form})