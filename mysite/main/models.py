from django.db import models

class Product():
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
