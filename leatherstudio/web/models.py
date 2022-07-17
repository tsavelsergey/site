import datetime
import image
from django.db import models
from django.utils import timezone
from PIL import Image


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    availability = models.BooleanField(default=True)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')

    def __str__(self):
        return self.name