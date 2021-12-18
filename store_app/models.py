from django.db import models
from django.urls.base import reverse
from category_app.models import Category

# Create your models here.
class Product(models.Model):
    product_name  = models.CharField(max_length=200, unique=True)
    slug          = models.SlugField(max_length=255, unique=True)
    description   = models.TextField(max_length=500, blank=True)
    price         = models.IntegerField()
    image         = models.ImageField(upload_to='photos/products')
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE)
    #models.CASCADE->whenever delete the category the products attached to that category will be deleted
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])


    def _str__(self):
        return self.product_name
