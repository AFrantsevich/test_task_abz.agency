import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "catalog_of_employee.settings")

import django
django.setup()

from employees.models import Person, PositionAtWork, Employee
from django_seed import Seed

seeder = Seed.seeder()


DATA_POSITION = {'CEO': [0, 1],
                 'Deputy CEO': [1, 40],
                 'Head Of Department': [2, 200],
                 'Deputy HOD': [3, 8000],
                 'Engineer': [4, 16759],
                 'Manager': [5, 25000]}

DATA_SALARY = {'CEO': 15000,
               'Deputy CEO': 10000,
               'Head Of Department': 8000,
               'Deputy HOD': 6000,
               'Engineer': 8000,
               'Manager': 5000}


def seed_person(seeder, amount_person):
    """The function populates the database's table 'Person'
    with random persons.
    Argument:
    amount_person(int) -- amount of person to be added to DB.
    """
    seeder.add_entity(Person, amount_person, {
        'first_name': lambda x: seeder.faker.first_name(),
        'last_name': lambda x: seeder.faker.last_name(),
        'middle_name': ""
    })
    seeder.execute()


def seed_position_at_work(seeder, data, model):
    """The function populates the database's table 'PositionAtWork'.
    For this function work there must be records in the table 'Person'
    Arguments:
    seeder -- the instance of seeder.
    data -- the dict:
        keys(str) represent position at work,
        values(list[int]) represent grade and amount of employees.
    model -- the Person's model.
    """

    id_employee = 1
    for position in data:
        amount_employees = data[position][1]
        grade = data[position][0]
        for i in range(0, amount_employees):
            seeder.add_entity(PositionAtWork, 1, {
                'position_name': f'{position} {i}',
                'grade': grade,
                'bio': model.objects.get(id=id_employee)
            })

            id_employee += 1
    seeder.execute()


def seed_employee(data, positionatwork, employee):
    """The function populates the database's table 'Employee'.
    For this function work there must be records in the tables 'Person'
    and 'PositionAtWork'.
    Arguments:
    data -- the dict:
        keys(str) represent position at work,
        values(int) represent a salary.
    positionatwork -- the PositionAtWork's model.
    employee -- the Employee's model.
    """

    for position in data:
        flag = True
        list_of_employees = (positionatwork.objects.
                             filter(position_name__startswith=position))
        list_of_parents = (employee.objects.
                           filter(position__grade=list_of_employees[0].grade - 1))
        if not list_of_parents:
            flag = False
            list_of_parents = list_of_employees
        amount_employees = len(list_of_employees) - 1

        while amount_employees != -1:
            for idx in range(len(list_of_parents)):
                if amount_employees == -1:
                    break
                employee.objects.create(**{
                    'salary': f'{data[position]}',
                    'position': list_of_employees[amount_employees],
                    'parent': list_of_parents[idx]
                    if len(list_of_parents) != len(list_of_employees)
                       and flag else None
                })
                amount_employees -= 1


if __name__ == '__main__':
    seed_person(seeder, 50000)
    seed_position_at_work(seeder, DATA_POSITION, Person)
    seed_employee(DATA_SALARY, PositionAtWork, Employee)
