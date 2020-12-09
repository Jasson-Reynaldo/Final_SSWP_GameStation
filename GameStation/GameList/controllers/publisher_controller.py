from django.shortcuts import render
from GameList.models.publisher import Publisher

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        publishers = Publisher.objects.filter(name__contains=name)
    else:
        publishers = Publisher.objects.all()
    data = {
        'publishers': publishers,
    }
    return render(request, 'publisher/index.html', context=data)
