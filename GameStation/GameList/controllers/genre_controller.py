from django.shortcuts import render
from GameList.models.genre import Genre
from GameList.forms.genre import GenreForm
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        genres = Genre.objects.all()
        if name and choice:
            if choice == 'name':
                genres = genres.filter(name__icontains=name)
            elif choice == 'description':
                genres = genres.filter(description__icontains=name)  
    else:
        genres = Genre.objects.all()
    paginator = Paginator(genres, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'genre/index.html', data)

@login_required
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('genre_index'))
    else:
        form = GenreForm()

    context = {
        'form': form
    }
    return render(request, 'genre/genre_form.html', context=context)

@login_required
def edit_genre(request, genre_id):
    if request.method == 'POST':
        genre = Genre.objects.get(pk=genre_id)
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('genre_index'))
    else:
        genre = Genre.objects.get(pk=genre_id)
        fields = model_to_dict(genre)
        form = GenreForm(initial=fields, instance=genre)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'genre/genre_form.html', context=context)

@login_required
def delete_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return HttpResponseRedirect(reverse('genre_index'))
    context = {
        'genre': genre,
    }
    return render(request, 'genre/genre_delete.html', context=context)
    