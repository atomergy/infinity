from django.contrib.auth.views import LoginView

from .forms import LoginForm

# Create your views here.


class NormalizedLoginView(LoginView):
    """
    This class is made only to make it easier for developers to manage templates. You can delete the "Normalized" models
    and save the Templates in the central registration directory (BASE_DIR / "templates").
    """
    template_name = "accounts/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']  # get remember me data from cleaned_data of form
        if not remember:
            self.request.session.set_expiry(0)  # if remember me is
            self.request.session.modified = True
        return super(NormalizedLoginView, self).form_valid(form)
