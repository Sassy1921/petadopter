from django.db import models

# Create your models here.


from distutils.command.upload import upload
from pickle import TRUE
from turtle import mode
from typing_extensions import Required
from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

ANIMAL_CHOICES = (
    ('Cat','CAT'),
    ('Dog','DOG'),
    ('Bird','BIRD'),
)
GENDER_CHOICES = (
    ('Female','FEMALE'),
    ('Male','MALE'),
)
LOGEMENT_CHOICES = (
    ('With Garden', 'with garden'),
    ('Without Garden', 'without garden'),

)
SITUATION_FAMILIALE_CHOICES = (
    ('Married',"married"),
    ('Divorced','divorced'),
    ('Separated','separated'),
    ('Single','single'),
    ('Widow(er)','widow(er)')
)

class Animal(models.Model):
    name = models.CharField(max_length=32)
    age = models.FloatField()
    statut_vaccinal = models.CharField(max_length=500)
    sterilisation = models.BooleanField(default=TRUE)
    image = models.ImageField(upload_to='media/')
    difficulty = models.IntegerField(
        validators= [MinValueValidator(1),MaxValueValidator(5)]
    )
    animal = models.CharField(choices=ANIMAL_CHOICES, max_length=4)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6)
    
    def __str__(self):
        return self.name
class Contact(models.Model):
    full_name = models.CharField(max_length=100,blank=False, null=False)
    email = models.EmailField(max_length=254,blank=False, null=False)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.full_name