from django.db import models

class Order(models.Model):
	dish = models.CharField(max_length=180, null=True, blank=True)
	address = models.CharField(max_length=180, null=True, blank=True)
