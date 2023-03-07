from django.urls import path
from accounts.views import login_


urlpatterns = [
    path("login/", login_, name="login"),
]