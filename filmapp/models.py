from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Aktyor(models.Model):
    ism = models.CharField(max_length=50,blank=True)#
    davlat = models.CharField(max_length=30, blank=True)
    jins = models.CharField(max_length=5, blank=True)
    tugulgan_yil = models.DateField(null=True)
    def __str__(self): return self.ism


class Kino(models.Model):
    nom = models.CharField(max_length=50,blank=True)#
    janr = models.CharField(max_length=50, blank=True)#
    yil = models.DateField(null=True)
    reyting = models.FloatField(null=True)#
    aktyorlar = models.ManyToManyField(Aktyor, blank=True)#
    def __str__(self): return self.nom


class Izohlar(models.Model):
    izoh_matni = models.CharField(max_length=30, blank=True)#
    sana = models.DateTimeField(auto_now_add=True, null=True)#
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE) #
    user = models.ForeignKey(User, on_delete=models.CASCADE)#
    def __str__(self): return self.kino.nom
