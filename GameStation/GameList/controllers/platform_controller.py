from django.shortcuts import render
from GameList.models.platform import Platform

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        platforms = Platform.objects.all()
        if name and choice:
            if choice == 'name':
                platforms = platforms.filter(name__contains=name)
            elif choice == 'creator':
                platforms = platforms.filter(creator__contains=name)  
    else:
        platforms = Platform.objects.all()
    data = {
        'platforms': platforms,
    }
    return render(request, 'platforms/index.html', context=data)
