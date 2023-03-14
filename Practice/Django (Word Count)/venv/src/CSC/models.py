from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    timezone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "<" + self.name + "-" + self.code + ">"


class State(models.Model):
    name = models.CharField(unique=True, max_length=50)
    code = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    timezone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "<" + self.name + "-" + self.code + ">"