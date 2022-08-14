# Generated by Django 4.0.6 on 2022-08-13 23:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It is name of human', max_length=200, verbose_name='Name')),
                ('age', models.PositiveIntegerField(help_text='How old this human',
                                                    validators=[django.core.validators.MaxValueValidator(150)],
                                                    verbose_name='Age')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
