from django import forms
from django.contrib.auth.models import User
from .models import Alumno, Profesor
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    #Este modelo ya incluye: username, first_name and email
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite tu contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class AlumnoEditForm(forms.ModelForm):
    class Meta:
         model = Alumno
         fields = ['num_boleta', 'carrera', 'plan', 'nombre_protocolo', 'es_alumno']
class ProfesorEditForm(forms.ModelForm):
    class Meta:
         model = Profesor
         fields = ['matricula', 'materias', 'es_profesor']