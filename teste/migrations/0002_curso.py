# Generated by Django 4.2.9 on 2024-01-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('carga_horaria', models.FloatField(max_length=4)),
                ('investimento', models.FloatField(max_length=4)),
            ],
        ),
    ]
