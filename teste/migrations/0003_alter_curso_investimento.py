# Generated by Django 4.2.9 on 2024-01-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0002_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='investimento',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
