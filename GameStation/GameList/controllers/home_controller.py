from django.shortcuts import render
from GameList.models.game import Game, Genre, Developer, Publisher, Platform, Official_web

def index(request):
    num_games = Game.objects.all().count()
    num_developers = Developer.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_platforms = Platform.objects.all().count()
    num_publishers = Publisher.objects.all().count()
    num_official_webs = Official_web.objects.all().count()
    context = {
        'num_games': num_games,
        'num_developers': num_developers,
        'num_genres': num_genres,
        'num_platforms': num_platforms,
        'num_publishers': num_publishers,
        'num_official_webs' : num_official_webs,
    }
    return render(request, 'home.html', context=context)

