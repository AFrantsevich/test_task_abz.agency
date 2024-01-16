# Generated by Django 5.0.1 on 2024-01-15 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='employees.positionatwork'),
        ),
        migrations.AlterField(
            model_name='positionatwork',
            name='bio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='positionatwork', to='employees.person'),
        ),
    ]
