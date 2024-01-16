
from django.urls import path
from . import views
from .views import Index

app_name = 'employees'

urlpatterns = [
    path("", Index.as_view(), name="index"),
]
