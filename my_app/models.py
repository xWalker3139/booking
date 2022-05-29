from django.db import models
from django.contrib.auth.models import User

RASPUNSURI = (
    ('Da', 'Da'),
    ('Nu', 'Nu'),
)

class Contact(models.Model):
    nume = models.CharField(max_length=264, null=True, blank=False)
    prenume = models.CharField(max_length=264, null=True, blank=False)
    mesaj = models.TextField(max_length=100000, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    telefon = models.FloatField(null=True, blank=False)

    def __str__(self):
        return self.nume

class Desk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tara = models.CharField(max_length=264, null=True, blank=False)
    oras = models.CharField(max_length=264, null=True, blank=False)
    strada = models.CharField(max_length=264, null=True, blank=False)
    etaj = models.FloatField(max_length=264, null=True, blank=False)
    imagine = models.ImageField(null=True, blank=False, upload_to="images")

    def __str__(self):
        return self.tara

class Places(models.Model):
    favorit = models.ManyToManyField(User, related_name='favorit', blank=True)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(null=True, blank=False)
    image = models.ImageField(null=True, blank=False, upload_to="images")
    desk = models.CharField(max_length=264, null=True, blank=False)

    def __str__(self):
        return self.desk or ''

class Answer(models.Model):
    option1 = models.CharField(max_length=264, null=True, blank=False, choices=RASPUNSURI)
    option2 = models.CharField(max_length=264, null=True, blank=False, choices=RASPUNSURI)
    option3 = models.CharField(max_length=264, null=True, blank=False, choices=RASPUNSURI)
    option4 = models.CharField(max_length=264, null=True, blank=False, choices=RASPUNSURI)

    def __str__(self):
        return self.option1

# Create your models here.
