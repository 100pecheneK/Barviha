from django.db import models

class room(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    title = models.CharField(max_length=255, default='', blank=True)
    title = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return '%s' % self.title
