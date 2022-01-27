from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=1200)

    def __str__(self):
        return self.title

    @classmethod
    def create(cls, title, content):
        post = cls(title=title, content=content)
        return post
