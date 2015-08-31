from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=200)
    clean_name = models.CharField(max_length=200)
    grouped_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    clean_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.address

class Grouping(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.address
