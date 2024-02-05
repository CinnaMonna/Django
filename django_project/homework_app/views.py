from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging
from homework_app.models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timezone
from .forms import ProductUpdateForm

logger = logging.getLogger(__name__)

def index1(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок</title>
</head>
<body>
    <h1>Это главная страница</h1>
</body>
</html>
    """
    logger.debug('Index page requested')
    
    return HttpResponse(html)


def about1(request: HttpRequest):
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок</title>
</head>
<body>
    <h1>Это страница обо мне</h1>
</body>
</html>
    """
    logger.debug('About page requested')

    return HttpResponse(html)


def clients_view(request):
    clients = Client.objects.all()

    res_str = '<br>'.join([str(client) for client in clients])

    return HttpResponse(res_str)


def orders_by_client_id(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    context = {'client' : client,
               'orders' : orders}
    return render(request, "homework_app/orders_by_client_id.html", context)

def products_by_order_id(request, order_id):
    order = Order.objects.get(id=order_id)
    products = order.products.all()

    context = {'order' : order,
               'products' : products}
    return render(request, "homework_app/products_by_order_id.html", context)


def products_by_client_id(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client=client)
    
    now = datetime.now(timezone.utc)
    products1 = []
    products2 = []
    products3 = []
    for order in orders:
        delta = now - order.order_date
        if delta.days <= 7:
            product = order.products.all()
            products1.append({product : order.order_date})
        elif delta.days <= 30:
            product = order.products.all()
            products2.append({product : order.order_date})
        elif delta.days <= 365:
            product = order.products.all()
            products3.append({product : order.order_date})

    context = {'client' : client,
               'products1' : products1,
               'products2' : products2,
               'products3' : products3,
               }
    return render(request, "homework_app/sorted_products_by_client_id.html", context)


def product_update(request):
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            choice_product = form.cleaned_data['choice_product_to_update']


            logger.info(f'Получили данные для обновления товара: {title}')

            product = Product.objects.get(id=choice_product.id)
            product.title = title
            product.description = description
            product.price = price
            product.save()
            message = 'Товар обновлен'

    else:
        form = ProductUpdateForm()
        message = 'Заполните форму'
    return render(request, 'homework_app/product_update_form.html', {'form' : form, 'message' : message})

