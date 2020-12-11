from django.shortcuts import render
from GameList.models.game import Game
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice_name = search['choice_name']
        choice_price = search['choice_price']
        price = search['price']
        games = Game.objects.all()
        if choice_name and name:
            if choice_name == 'title':
                games = games.filter(title__icontains=name)
            elif choice_name == 'genre':
                games = games.filter(genre__name__icontains=name)
            elif choice_name == 'developer':
                games = games.filter(developer__last_name__icontains=name) | games.filter(developer__first_name__icontains=name)
            elif choice_name == 'publisher':
                games = games.filter(publisher__name__icontains=name)
            elif choice_name == 'official_web':
                games = games.filter(offical_web__name__icontains=name)
            elif choice_name == 'platform':
                games = games.filter(platform__name__icontains=name)
     
        if choice_price and price:
            if choice_price == 'equal':
                games = games.filter(price=price)
            elif choice_price == 'less_than':
                games = games.filter(price__lt=price)
            elif choice_price == 'less_than_equal':
                games = games.filter(price__lte=price)
            elif choice_price == 'greater_than':
                games = games.filter(price__gt=price)
            elif choice_price == 'greater_than_equal':
                games = games.filter(price__gte=price)             
    else:
        games = Game.objects.all()
    paginator = Paginator(games, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'game/index.html', data)
