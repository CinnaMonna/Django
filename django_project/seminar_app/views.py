from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('index get request')
    return HttpResponse('Hello, World!')

def heads_tails(request):
    heads_tails_str = ['Tails', 'Heads']
    side = choice(heads_tails_str)
    logger.info(f'heads/tails side is: {side}')
    return HttpResponse(side)

def dice(request):
    dice_side = randint(1, 6)
    logger.info(f'dice side is: {dice_side}')
    return HttpResponse(dice_side)

def random_number(request):
    random_number = randint(0, 100)
    logger.info(f'random number is: {random_number}')
    return HttpResponse(random_number)


