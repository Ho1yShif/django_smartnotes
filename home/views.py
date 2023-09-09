from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins	import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

class SignupView(CreateView):
	form_class = UserCreationForm
	template_name = 'home/register.html'
	success_url = '/smart/notes'

	"""Override the built-in get method so that only unauthenticated users can access the signup page"""
	def get(self, request, *args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('notes.list')
		return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
	template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
	template_name = 'home/login.html'
	
class HomeView(TemplateView):
	template_name = 'home/welcome.html'
	extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
	template_name = 'home/authorized.html'
	login_url = '/admin'

		# FILEPATH: /Users/shifra.isaacs/Documents/Repos/class_practice/django_smartnotes/home/views.py

def welcome(request):
	context = {
		'datetime': datetime.datetime.now()
	}
	return render(request, 'home/welcome.html', context)
