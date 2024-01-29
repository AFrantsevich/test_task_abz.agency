from django.urls import path

from .views import Index, EmployeeView

app_name = 'employees'

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("<int:id>/", EmployeeView.as_view(), name="employee"),
]
