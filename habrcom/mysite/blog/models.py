from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) #Заголовок
    datetime = models.DateTimeField(auto_now_add=True) #Дата
    content = models.TextField(max_length=10000) #Текст

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id