# Generated by Django 3.2.5 on 2021-08-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nome')),
                ('category', models.CharField(max_length=128, verbose_name='Categoria')),
                ('value', models.FloatField(verbose_name='valor')),
                ('type', models.CharField(max_length=32, verbose_name='Tipo')),
                ('expiry_date', models.DateField(blank=True, null=True, verbose_name='Data de Validade')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('inventory_alert', models.BooleanField(verbose_name='Alerta de Estoque')),
                ('set_date', models.DateField(blank=True, null=True, verbose_name='Data de Marcação')),
                ('set_time', models.TimeField(blank=True, null=True, verbose_name='Hora de Marcação')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'ordering': ['id'],
            },
        ),
    ]