from django.shortcuts import render
from GameList.models.genre import Genre

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        genres = Genre.objects.filter(name__contains=name)
    else:
        genres = Genre.objects.all()
    data = {
        'genres': genres,
    }
    return render(request, 'genre/index.html', context=data)