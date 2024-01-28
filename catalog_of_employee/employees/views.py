from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .models import Employee
from .tables import EmployeeTable
from .filters import ProductFilter


class Index(SingleTableMixin, FilterView):
    template_name = "base.html"
    table_class = EmployeeTable
    queryset = Employee.objects.all()
    filterset_class = ProductFilter

    def get_template_names(self):
        if self.request.htmx:
            template_name = "includes/table.html"
        else:
            template_name = "base.html"

        return template_name
