# Generated by Django 4.0.2 on 2022-03-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('activo', models.BooleanField()),
            ],
        ),
    ]