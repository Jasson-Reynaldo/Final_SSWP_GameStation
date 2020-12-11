from django.shortcuts import render
from GameList.models.game import Game
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        price = search['price']
        games = Game.objects.all()
        if name:
            games = games.filter(title__icontains=name)
        if choice and price:
            if choice == 'equal':
                games = games.filter(price=price)
            elif choice == 'less_than':
                games = games.filter(price__lt=price)
            elif choice == 'less_than_equal':
                games = games.filter(price__lte=price)
            elif choice == 'greater_than':
                games = games.filter(price__gt=price)
            elif choice == 'greater_than_equal':
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
