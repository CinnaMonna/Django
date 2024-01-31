# from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Coin
from seminar_app.models import Author, Post
from django.shortcuts import render

logger = logging.getLogger(__name__)

def index(request): 
    context = {'title' : 'главная страница'}
    logger.info('index get request')
    return render(request, "seminar_app/index.html", context)


def about(request): 
    context = {'name' : 'Наталья'}
    logger.info('about get request')
    return render(request, "seminar_app/about.html", context)


def heads_tails(request, count):
    result_list = []
    for i in range(count):
        side = choice(['Tails', 'Heads'])
        logger.info(f'heads/tails side is: {side}')
        result_list.append(side)
    
    context = {'result_list' : result_list,
               'title' : 'Heads & tails'}

    # if side == 'Tails':
    #     res = 1
    # else:
    #     res = 0

    # coin = Coin(side=res)
    # coin.save()

    # my_dict = Coin.get_data(5)
     
    # return HttpResponse(f'Side is: {side}, {my_dict}')

    return render(request, 'seminar_app/game_result.html', context)


def dice(request, count):
    result_list = []
    for i in range(count):
        dice_side = randint(1, 6)
        logger.info(f'dice side is: {dice_side}')
        result_list.append(dice_side)
    
    context = {'result_list' : result_list,
               'title' : 'Dice'}
    
    return render(request, 'seminar_app/game_result.html', context)


def random_number(request, count):
    result_list = []
    for i in range(count):
        random_number = randint(0, 100)
        logger.info(f'random number is: {random_number}')
        result_list.append(random_number)
    
    context = {'result_list' : result_list,
               'title' : 'Random number'}
    
    return render(request, 'seminar_app/game_result.html', context)

 
def authors_view(request):
    authors = Author.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)


def post_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)


def authors_posts_list(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)

    context = {'posts_list' : posts,
               'author' : author}

    return render(request, 'seminar_app/authors_posts_list.html', context)


def post(request, post_id):
    post1 = Post.objects.get(id=post_id)
    context = {'post1' : post1}
    return render(request, 'seminar_app/post.html', context) 