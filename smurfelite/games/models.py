from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Games Name')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    game = models.ForeignKey(Games, related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Category Name')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.game} -- {self.name}"

class Product(models.Model):
    game = models.ForeignKey(Games, related_name='product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Product Name')
    price = models.FloatField()
    intro = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    steam_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 