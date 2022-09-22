from django.contrib.auth.views import LoginView
from django.views import generic

from .forms import LoginForm, NormalizedRegisterForm

# Create your views here.

class NormalizedRegisterView(generic.edit.CreateView):
    form_class = NormalizedRegisterForm
    template_name = "accounts/register.html"
