from django.db import models

class Image(models.Model):
    path = models.CharField(max_length=1000)
    name = models.CharField(max_length=255)
    ext = models.CharField(max_length=5)

    def __str__(self):
        return self.name + '/' + self.ext

class Category(models.Model):
    name = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ForeignKey(Image, on_delete=models.CASCADE)



