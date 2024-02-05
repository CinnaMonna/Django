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
    add_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self) -> str:
        return f'{self.title}, price: {self.price}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    summary_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Order of client: {self.client},  order cost: {self.summary_cost}, order date: {self.order_date}'

