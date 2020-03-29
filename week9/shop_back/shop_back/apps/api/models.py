from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField('Name of the category',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField('Name of the product',max_length=100)
    price=models.FloatField('Price of the product')
    description=models.TextField('Description of the product')
    count=models.IntegerField('Amount of the products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
