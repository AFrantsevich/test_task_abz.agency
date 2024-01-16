import datetime

from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class PositionAtWork(models.Model):
    position_name = models.CharField(max_length=128)
    grade = models.FloatField()
    bio = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        related_name='positionatwork',
        null=True
    )

    class Meta:
        ordering = ["grade"]

    def __str__(self):
        return self.position_name


class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128,
                                   blank=True)
    hire_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return (f"{self.first_name} "
                f"{self.last_name}")


class Employee(MPTTModel):
    salary = models.FloatField()
    position = models.ForeignKey(
        PositionAtWork,
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True
    )
    parent = TreeForeignKey('self',
                          on_delete=models.SET_NULL,
                          null=True, blank=True,
                          related_name='children')

    def __str__(self):
        return (f'{self.position.bio.first_name} '
                f'{self.position.bio.last_name} '
                f'{self.position.position_name}')

    class MPTTMeta:
        order_insertion_by = ['position']
