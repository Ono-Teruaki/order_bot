from django.db import models
from django.utils import timezone

# Create your models here.

class MenuGenre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    img = models.ImageField(upload_to='genre_images/')
    
    class Meta:
        verbose_name = 'ジャンル'
        verbose_name_plural = 'ジャンル'

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField()
    img = models.ImageField(upload_to='menu_images/')
    genre = models.ForeignKey(MenuGenre, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name = 'メニュー'
        verbose_name_plural = 'メニュー'

    def __str__(self):
        return self.name
    
    
class Log(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = '注文履歴'
        verbose_name_plural = '注文履歴'
    
    def __str__(self):
        return f'{self.menu.name}  {self.menu.price}円'