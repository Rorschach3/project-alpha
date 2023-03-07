from django.urls import path
from accounts.views import login_, logout_


urlpatterns = [
    path("login/", login_, name="login"),
    path("logout/", logout_, name="logout"),
]