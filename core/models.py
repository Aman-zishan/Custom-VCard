from django.db import models
from django.conf import settings


class Profile(models.Model):
    title = models.CharField(max_length=100)
    profile_image = models.ImageField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    gallery_images = models.ImageField()

    def __str__(self):
        return self.title
