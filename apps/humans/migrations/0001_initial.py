# Generated by Django 4.0.6 on 2022-08-26 16:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of color', max_length=35, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='It is name of human', max_length=200, verbose_name='Name')),
                ('age', models.PositiveIntegerField(help_text='How old this human', validators=[django.core.validators.MaxValueValidator(150)], verbose_name='Age')),
                ('favourite_color', models.CharField(choices=[('black', 'black'), ('white', 'White'), ('red', 'Red')], default='white', max_length=35, verbose_name='Favourite color')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('favourite_color_by_foreign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='humans_related_by_foreign_key', to='humans.color')),
                ('favourite_color_many_to_many', models.ManyToManyField(related_name='humans_related_many_to_many_items', to='humans.color')),
            ],
        ),
        migrations.CreateModel(
            name='SuperHuman',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='humans.human')),
                ('level', models.PositiveIntegerField(help_text='Level of power', verbose_name='Level')),
            ],
            bases=('humans.human',),
        ),
    ]
