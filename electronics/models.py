from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    code = models.CharField(max_length=10,
                            null=False,
                            blank=False)
    
    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)
    
    def __str__(self) -> str:
        return self.code
    

class Product(models.Model):
    product_id = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)
    
    category_code = models.CharField(max_length=10,
                                     null=False,
                                     blank=False)
    
    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)
    
    quantity_available = models.IntegerField(null=False,
                                             blank=False)
    
    cost = models.DecimalField(max_digits=10,
                               decimal_places=2,
                               null=False,
                               blank=False)
    
    selling_price = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    
    def __str__(self) -> str:
        return self.product_id
    
class Customer(models.Model):
    customer_id = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)
    
    firstname = models.CharField(max_length=50,
                                  null=False,
                                  blank=False)
    
    lastname = models.CharField(max_length=50,
                                 null=False,
                                 blank=False)
    
    address = models.CharField(max_length=100,
                               null=False,
                               blank=False)
    
    date_of_birth = models.DateField(null=False,
                                     blank=False)
    
    email = models.EmailField(max_length=100,
                              null=False,
                              blank=False)
    
    home_phone = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)
    
    cell_phone = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)
    
    def __str__(self) -> str:
        return f'{self.customer_id} {self.firstname} {self.lastname}'
    
class Order(models.Model):
    order_number = models.IntegerField(null=False,
                                       blank=False)
    
    customer_id = models.CharField(max_length=10,
                                   null=False,
                                   blank=False)
    
    order_date = models.DateField(null=False,
                                  blank=False)
    
    shipped_date = models.DateField(null=False,
                                    blank=False)
    
    payment_date = models.DateField(null=False,
                                    blank=False)
    
    def __str__(self) -> str:
        return f'{self.order_number} {self.customer_id}'
    
class OrderDetail(models.Model):
    order_number = models.IntegerField(null=False,
                                       blank=False)
    
    product_id = models.CharField(max_length=10,
                                  null=False,
                                  blank=False)
    
    def __str__(self) -> str:
        return f'{self.order_number} - {self.product_id}'
