from django.contrib.auth.views import LoginView

# Create your views here.


class NormalizedLoginView(LoginView):
    """
    This class is made only to make it easier for developers to manage templates. You can delete the "Normalized" models
    and save the Templates in the central registration directory (BASE_DIR / "templates").
    """
    template_name = "accounts/login.html"
