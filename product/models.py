from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, related_name='child_categories', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    objects = None
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

