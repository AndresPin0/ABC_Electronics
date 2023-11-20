from django.db import models


class CategoryProduct(models.Model):
    code = models.CharField(primary_key=True,
                            max_length=10,
                            null=False,
                            blank=False)

    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)

    def __str__(self) -> str:
        return f'{self.code} - {self.description}'


class Product(models.Model):
    product_id = models.CharField(primary_key=True,
                                  max_length=10,
                                  null=False,
                                  blank=False)

    category_code = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)

    description = models.CharField(max_length=100,
                                   null=False,
                                   blank=False)

    quantity_available = models.IntegerField(null=False,
                                             blank=False)

    cost = models.DecimalField(max_digits=100,
                               decimal_places=2,
                               null=False,
                               blank=False)
    
    selling_price = models.DecimalField(max_digits=100,
                                        decimal_places=2,
                                        null=False,
                                        blank=False)
    
    referential_image_path = models.CharField(max_length=1000,
                                              null=True)
    
    def __str__(self) -> str:
        return f'{self.product_id} - {self.description}'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True,
                                   max_length=10,
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

    date_of_birth = models.DateTimeField(null=False,
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
        return f'{self.customer_id} - {self.firstname} {self.lastname}'


class Order(models.Model):
    order_number = models.AutoField(primary_key=True)

    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    order_date = models.DateTimeField(null=False,
                                      blank=False)

    shipped_date = models.DateTimeField(null=False,
                                        blank=False)

    payment_date = models.DateTimeField(null=False,
                                        blank=False)

    def __str__(self) -> str:
        return f'{self.order_number} - {self.customer_id}'


class OrderDetail(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('order_number', 'product_id')

    def __str__(self) -> str:
        return f'{self.order_number} - {self.product_id}'
