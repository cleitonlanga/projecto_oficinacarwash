# Generated by Django 5.0.2 on 2024-02-26 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='carrro',
            new_name='carro',
        ),
    ]
