# Generated by Django 4.2.3 on 2023-08-15 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('detalle', models.TextField(blank=True)),
            ],
        ),
    ]
