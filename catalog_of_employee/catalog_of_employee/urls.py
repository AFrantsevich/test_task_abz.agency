from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("employees/", include("employees.urls", namespace='employees')),
    path('admin/', admin.site.urls),
]
