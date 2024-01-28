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

    return f'padding-left:{PADDING_BY_GRADE[data.position.grade]}px'


class EmployeeTable(tables.Table):
    position__bio__first_name = tables.Column(
        verbose_name='First Name',
        attrs={"td": {"style": get_padding_position}})
    position__bio__last_name = tables.Column(
        verbose_name='Last Name',
        attrs={"td": {"style": get_padding_position}})
    position__position_name = tables.Column(
        verbose_name='Position At Work',
        attrs={"td": {"style": get_padding_position}})
    position__bio__hire_date = tables.Column(
        verbose_name='Hire Date')

    class Meta:
        template_name = "includes/table.html"
