from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='categories')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.name



class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    class Meta:
        ordering = ['created']



class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    class Meta:
        ordering = ['created']
