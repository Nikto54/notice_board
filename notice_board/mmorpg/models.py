from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField



class Author(models.Model):
    name=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name.username

class Category(models.Model):
    name=models.CharField(max_length=64,null=True)

    def __str__(self):
        return self.name

class Notice(models.Model):
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.CharField(max_length=64)
    content=RichTextUploadingField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Response(models.Model):
    article = models.CharField(max_length=64)
    text = models.TextField(max_length=255)
    notice = models.ForeignKey(Notice, related_name='responses', on_delete=models.CASCADE)

    def __str__(self):
        return self.article





