from django.urls import path

from . import views

# Create your custom views here.

app_name = "accounts"

urlpatterns = [
    path("login/", views.NormalizedLoginView.as_view(), name="login"),
]
