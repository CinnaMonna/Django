from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}'
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}, price: {self.price}, count: {self.count}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Order {self.order_sum}, order date: {self.order_date}'
