from django.db import models

from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Post Title')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField(verbose_name='Post Content')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0, verbose_name='Post Status')

    class Meta:
        ordering = ['-created_on', 'author']

    def __str__(self):
        return f"The title of this post is: {self.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Commenter')
    body = models.TextField(verbose_name='Comment')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False, verbose_name='Approved')

    class Meta:
        ordering = ['-created_on',]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

