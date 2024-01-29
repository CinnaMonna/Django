# from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Coin
from seminar_app.models import Author, Post

logger = logging.getLogger(__name__)

def index(request):
    logger.info('index get request')
    return HttpResponse('Hello, World!')

def heads_tails(request):
    heads_tails_str = ['Tails', 'Heads']
    side = choice(heads_tails_str)

    if side == 'Tails':
        res = 1
    else:
        res = 0

    logger.info(f'heads/tails side is: {side}')

    coin = Coin(side=res)
    coin.save()

    my_dict = Coin.get_data(5)
     
    return HttpResponse(f'Side is: {side}, {my_dict}')

def dice(request):
    dice_side = randint(1, 6)
    logger.info(f'dice side is: {dice_side}')
    return HttpResponse(dice_side)

def random_number(request):
    random_number = randint(0, 100)
    logger.info(f'random number is: {random_number}')
    return HttpResponse(random_number)

 
def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)

def post_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)