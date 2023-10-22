from django.shortcuts import render
from django.http import HttpResponse
import logging
from myapp2.models import Product

logger = logging.getLogger(__name__)

def index(request):
    product = Product.objects.all()

    logger.info(f'Показана информация: {product}')
    return render(request, 'myapp/index.html', {'products': product})
def about(request):
    html = "<h1>About us</h1>" \
           "<p>Страница о нас</p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)

