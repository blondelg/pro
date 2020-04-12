from django.db import models

ORDER = [(a,a) for a in range(1,21)]

# Create your models here.
class About(models.Model):
    abo_icon = models.CharField(max_length=60)
    abo_title = models.CharField(max_length=30)
    abo_description = models.TextField()
    abo_order = models.IntegerField(choices=ORDER, default=20)
    abo_display = models.BooleanField(default=False)

class Experience(models.Model):
    exp_compagny_name = models.CharField(max_length=30)
    exp_geo = models.CharField(max_length=30)
    exp_start = models.DateField()
    exp_stop = models.DateField()
    exp_order = models.IntegerField(choices=ORDER, default=20)
    exp_display = models.BooleanField(default=False)

class Projet(models.Model):
    pro_title = models.CharField(max_length=30)
    pro_year = models.IntegerField(default=2020)
    pro_description = models.TextField()
    pro_order = models.IntegerField(choices=ORDER, default=20)
    pro_display = models.BooleanField(default=False)

# class Skill(models.Model):
#     ski_name =
#     ski_level =
#     ski_type =
#     ski_order = models.IntegerField(choices=ORDER, default=20)
#     ski_display = models.BooleanField(default=False)

class Study(models.Model):
    pass

class Image(models.Model):
    pass

class SkillType(models.Model):
    pass
