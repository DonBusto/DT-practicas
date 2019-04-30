from django.db import models

class Activity(models.Model):
    cnae = models.IntegerField(primary_key=True, verbose_name="CNAE[#]")
    peso = models.FloatField(verbose_name="PESO [kg]")



