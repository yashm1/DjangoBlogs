import datetime

from django.db import models
from django.utils import timezone


class BlogContent(models.Model):
    post_title = models.CharField( verbose_name='Title', max_length=200, default="Blog post", primary_key=True )
    post_desc = models.TextField( verbose_name='Description', max_length=100 )
    post_text = models.TextField( verbose_name='Story')
    post_date = models.DateField( verbose_name='Date published' )
    post_img = models.ImageField( verbose_name='Thumbnail' ,default="hello",upload_to="blogger/static/Images")
    featured = models.BooleanField( default=False )


class Comment(models.Model):
    Comment = models.ForeignKey(BlogContent, on_delete=models.CASCADE)
    Comment_user=models.CharField(max_length=200)
    Comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)