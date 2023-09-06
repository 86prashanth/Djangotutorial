from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200, null= True)
    product_description = models.CharField(max_length=1000, null= True)
    no_product_orders = models.PositiveIntegerField(null= True)
    product_rating = models.PositiveSmallIntegerField(null= True)
    product_image = models.URLField(null=True)

    def __str__(self):
        return self.product_name