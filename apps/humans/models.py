from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField('Name', help_text='It is name of human', max_length=200)
    age = models.PositiveIntegerField('Age', help_text='How old this human', validators=[MaxValueValidator(150)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
