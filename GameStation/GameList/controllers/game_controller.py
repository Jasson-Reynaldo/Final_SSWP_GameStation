from django.shortcuts import render
from GameList.models.game import Game

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        price = search['price']
        games = Game.objects.all()
        if name:
            games = games.filter(name__contains=name)
        if choice and price:
            if choice == 'equal':
                games = games.filter(price=price)
            elif choice == 'less_than':
                games = games.filter(price_lt=price)
            elif choice == 'less_than_equal':
                games = games.filter(price_lte=price)
            elif choice == 'greater_than':
                games = games.filter(price_gt=price)
            elif choice == 'greater_than_equal':
                games = games.filter(price_gte=price)        
    else:
        games = Game.objects.all()
    data = {
        'games': games,
    }
    return render(request, 'game/index.html', context=data)
