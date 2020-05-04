from django.db import models

# Create your models here.
class personnalInfo(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    age = models.DecimalField(max_digits=3,decimal_places=0)
    email = models.EmailField()
    littleImage = models.CharField(max_length=120,null=True,blank=True)
    bigImage = models.CharField(max_length=120,null=True,blank=True)
    summary = models.TextField(max_length=200,null=True,blank=True)
    Address = models.CharField(max_length=120,null=True,blank=True)

class skillsInfo(models.Model):
    skillName = models.CharField(max_length=120,null=True,blank=True)
    skillimg = models.CharField(max_length=120,null=True,blank=True)


class diplomaInfo(models.Model):
    nameDiploma = models.CharField(max_length=120,null=True,blank=True)
    yearDiploma = models.CharField(max_length=120,null=True,blank=True)
    InstituteDiploma = models.CharField(max_length=120,null=True,blank=True)

class ExperienceInfo(models.Model):
    title = models.CharField(max_length=120,null=True,blank=True)
    periodeStart = models.CharField(max_length=120,null=True,blank=True)
    periodeEnd = models.CharField(max_length=120,null=True,blank=True)
    info = models.TextField(max_length=120,null=True,blank=True)

class phoneInfo(models.Model):
    phoneNumber = models.CharField(max_length=120,null=True,blank=True)

class languageInfo(models.Model):
    language = models.CharField(max_length=120,null=True,blank=True)
    languageDetails = models.CharField(max_length=120,null=True,blank=True)
    percentage = models.IntegerField()

class hobbiesInfo(models.Model):
    hobbyInfo = models.CharField(max_length=120,null=True,blank=True)


