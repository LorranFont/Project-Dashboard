from django.db import models

# Create your models here.

class Product(models.Model) = 
    name = models.CharField(max_length=255)
    expiration_date = models.DateField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    

class stock(models.Model) = 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.available_quantity}'


class User(models.Model) = 
    username = models.Charfield(max_lenght=150, unique=True)
    password = models.CharFiel(max_length=128)

    def __str__(self):
        return self.username


class Sale(models.Model) = 

    product = models.ForeingKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    total_value = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.quantity_sold}'


class offer(models.Model) = 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discout = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'Offer: {self.product.name} - {self.discout}%'
     
    