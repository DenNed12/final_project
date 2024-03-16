from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.cache import cache



class Author(models.Model):
    authorUser = models.OneToOneField(User,on_delete= models.CASCADE)




class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='subscribers')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, null=False)
    postAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    text = models.TextField(default='Some Text')
    content = models.FileField(null  = True)

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.title}: {self.text[:20]}'

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        cache.delete(f'post-{self.pk}')


class Reply(models.Model):
    postReply = models.ForeignKey(Post, on_delete=models.CASCADE)
    authorReply = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField(default='Текст комментария')
    dateTime = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    postTrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryTrough = models.ForeignKey(Category, on_delete = models.CASCADE)
