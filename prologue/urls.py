from django.urls import path
from . import views

app_name = "prologue"
urlpatterns = [path("", views.home, name="home")]
