from django.urls import path
from accounts.views import login_, logout_, signup


urlpatterns = [
    path("login/", login_, name="login"),
    path("logout/", logout_, name="logout"),
    path("signup/", signup, name="signup"),
]
