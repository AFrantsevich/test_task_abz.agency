import django_tables2 as tables


PADDING_BY_GRADE = {0.0: 15, 1.0: 30,
                    2.0: 45, 3.0: 60,
                    4.0: 75, 5.0: 95}


def get_padding_position(**kwargs):
    """The function adds spaces to the string
    according to the grade to form a tree structure.
    If the table uses sort or search, spaces = 0.
    """

    request = kwargs.get("table", None).request.GET
    data = kwargs.get("record", None)
    if not data:
        return
    elif request.get('sort', False):
        return
    elif (not request.get('query') == ''
          and request.get('query', None) is not None):
        return

    return PADDING_BY_GRADE[data.position.grade]


def get_employee_id(**kwargs):
    result = None
    if kwargs.get('record', False):
        result = kwargs.get('record', False).id
    return result


def get_style(**kwargs):
    result = ''
    padding = get_padding_position(**kwargs)
    column = kwargs.get('bound_column', None)
    if column and (column.verbose_name == 'First Name' or column.verbose_name == 'Last Name'):
        result = f'padding-left:{padding}px; cursor:pointer;'
    return result


TD_ATTRS = {"style": get_style,
            # "hx-get": get_employee_id,
            # "hx-trigger": "click",
            # "hx-target": "div.container-fluid",
            # "hx-swap": "outerHTML",
            # "hx-push-url": "true"
            }

class EmployeeTable(tables.Table):
    position__bio__first_name = tables.Column(
        verbose_name='First Name',
        attrs={"td": TD_ATTRS})
    position__bio__last_name = tables.Column(
        verbose_name='Last Name',
        attrs={"td": TD_ATTRS})
    position__position_name = tables.Column(
        verbose_name='Position At Work',
        attrs={"td": {"style": get_padding_position}})
    position__bio__hire_date = tables.Column(
        verbose_name='Hire Date')

    class Meta:
        template_name = "includes/table.html"
        row_attrs = {
            "data-id": lambda record: record.pk
        }
