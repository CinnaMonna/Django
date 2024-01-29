from django.db import models

class Coin(models.Model):
    side = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f' fellOut: {self.side}, time: {self.time_created}'
    

    @staticmethod
    def get_data(count):
        coins = Coin.objects.all()[:count] 
        coins_dict = {
            'head': [],
            'tail': []
        }

        for coin in coins:
            if coin.side == 0:
                coins_dict['head'].append(coin.time_created)
            else:
                coins_dict['tail'].append(coin.time_created)
        return coins_dict
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def get_full_name(self):
        return f'{self.name} {self.last_name}'
    
    def __str__(self) -> str:
        return f'Author: {self.name} {self.last_name}, email: {self.email}'
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Post: {self.title}, Author: {self.author}'
    