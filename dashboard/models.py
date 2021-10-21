from django.db import models

# Create your models here.

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100 , null=True)
    category = models.CharField(max_length=20, choices=CATEGORY , null=True)
    quantity = models.PositiveIntegerField(null=True)
 
    # It shows how the thinkg gonna show on admin panel 
    # This return itself value like Milk-100 on admin panel
    def __str__(self):
        return f'{self.name}-{self.quantity}'