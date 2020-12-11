from django.shortcuts import render
from GameList.models.platform import Platform
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        platforms = Platform.objects.all()
        if name and choice:
            if choice == 'plat':
                platforms = platforms.filter(name__icontains=name)
            elif choice == 'creator':
                platforms = platforms.filter(creator__icontains=name)  
    else:
        platforms = Platform.objects.all()
    paginator = Paginator(platforms, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'platform/index.html', data)