from django.db import models

class Subscribers(models.Model):
        email = models.EmailField(
        unique = True,
    )
    
        first_name = models.CharField(
        max_length = 200,
        blank = True,
    )
    
        last_name = models.CharField(
        max_length = 200,
        blank = True,
    )
class apartment(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
    )

    text = models.CharField(
        max_length=200,
        blank=True,
    )

class rental(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
    )

    text = models.CharField(
        max_length=200,
        blank=True,
    )