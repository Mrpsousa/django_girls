# Generated by Django 3.2.4 on 2021-09-04 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Validade'),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory_alert',
            field=models.BooleanField(blank=True, null=True, verbose_name='Alerta de Estoque'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade'),
        ),
    ]