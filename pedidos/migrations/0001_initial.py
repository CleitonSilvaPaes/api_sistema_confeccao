# Generated by Django 4.1.3 on 2022-12-03 13:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
        ('cliente', '0001_initial'),
        ('usuario_sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_fiscal', models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9)])),
                ('data_entrega', models.DateField()),
                ('item', models.CharField(max_length=50)),
                ('valor', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('status_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.status')),
                ('user_sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_sistema.usuariosistema')),
            ],
        ),
    ]