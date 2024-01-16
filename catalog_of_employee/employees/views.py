from django.views import View
from .models import Employee
from django.shortcuts import render


class Index(View):
    template_name = "index2.html"

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, self.template_name,
                      {"employees": employees})
