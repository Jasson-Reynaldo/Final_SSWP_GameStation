from django.shortcuts import render
from GameList.models.genre import Genre
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        genres = Genre.objects.filter(name__contains=name)
    else:
        genres = Genre.objects.all()
    paginator = Paginator(genres, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'genre/index.html', data)