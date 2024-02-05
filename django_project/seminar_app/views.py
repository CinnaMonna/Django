# from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import Coin, Author, Post
from .forms import GameTypeForm, AuthorAddForm, PostAddFormWidget
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

# Создайте представление, которое выводит форму выбора. 
# В зависимости переданных значений представление вызывает одно из трёх представлений, 
# созданных на прошлом семинаре (если данные прошли проверку, конечно же).

def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            logger.info(f'Получили {game_type=}, {throws_number=}.')
            if game_type == 'C':
                return heads_tails(request, throws_number)
            elif game_type == 'D':
                return dice(request, throws_number)
            else:
                return random_number(request, throws_number)
        
    else:
        form = GameTypeForm()
    return render(request, 'seminar_app/games.html', {'form' : form})


def author_add(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            bio = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']

            logger.info(f'Получили данные {name}')

            author = Author(name=name, last_name=last_name, email=email, bio=bio, birthday=birthday)
            author.save()
            message = 'Автор сохранен'

    else:
        form = AuthorAddForm()
        message = 'Заполните форму'
    return render(request, 'seminar_app/author_form.html', {'form' : form, 'message' : message})


def post_add(request):
    if request.method == 'POST':
        form = PostAddFormWidget(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            is_published = form.cleaned_data['is_published']

            logger.info(f'Получили данные: статья {title}, автор {author}')

            post = Post(title=title, content=content, publish_date=publish_date, author=author, category=category, is_published=is_published)
            post.save()
            message = 'Статья сохранена'

    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'
    return render(request, 'seminar_app/post_form.html', {'form' : form, 'message' : message})
