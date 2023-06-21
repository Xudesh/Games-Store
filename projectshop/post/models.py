from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Названия')
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField(upload_to='post/images')
    price = models.DecimalField('Цена',max_digits=5, decimal_places=2, null=True, blank=True)
    author = models.ForeignKey(to=User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('postdetail', kwargs={'id': self.pk})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Пост'
        verbose_name = 'Посты'

class Comment(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    user = models.CharField('Имя', max_length=25)
    text = models.TextField('Коментария')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/images')

    def __str__(self):
        return self.user
    

class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/images/')

    def __str__(self):
        return f'Пользователь {self.user.username}'
    
    @property
    def full_name(self):
        return f'{self.user.username} with {self.date_of_birth}'