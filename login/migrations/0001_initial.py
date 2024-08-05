# Generated by Django 5.0.2 on 2024-05-06 12:47

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('profissao', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, default=None, null=True)),
                ('nationality', models.CharField(default='Moçambique', max_length=64)),
                ('province', models.CharField(default='Maputo', max_length=64)),
                ('bi', models.CharField(max_length=14)),
                ('city', models.CharField(default='Matola', max_length=128)),
                ('contact', models.CharField(blank=True, max_length=32)),
                ('joined_in', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]