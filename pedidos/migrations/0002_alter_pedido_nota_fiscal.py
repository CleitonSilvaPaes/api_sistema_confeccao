# Generated by Django 4.1.3 on 2022-12-05 21:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='nota_fiscal',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(9), django.core.validators.MinLengthValidator(4)]),
        ),
    ]
