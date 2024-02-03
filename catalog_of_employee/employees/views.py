from django.views import View
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.shortcuts import render

from .models import Employee
from .tables import EmployeeTable
from .filters import ProductFilter


class Index(SingleTableMixin, FilterView):
    template_name = "includes/tree.html"
    table_class = EmployeeTable
    queryset = Employee.objects.all()
    filterset_class = ProductFilter

    def get_template_names(self):
        if self.request.htmx:
            template_name = "includes/table.html"
        else:
            template_name = "includes/tree.html"

        return template_name


class EmployeeView(View):

    def get(self, request, *args, **kwargs):
        if self.request.htmx:
            self.template_name = "includes/user.html"
        else:
            self.template_name = "includes/user_info.html"

        employee = Employee.objects.get(id=kwargs.get('id'))
        return render(request, self.template_name,
                              {"employee": employee})


# from django.http import HttpResponse
# def your_view_name(request, *args, **kwargs):
#     print(request, args, kwargs, request.body)
#     return HttpResponse("Hello, World!")
