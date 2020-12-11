from django.shortcuts import render
from GameList.models.publisher import Publisher
from django.core.paginator import Paginator

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        publishers = Publisher.objects.all()
        if name and choice:
            if choice == 'name':
                publishers = publishers.filter(name__contains=name)
            elif choice == 'founder_name':
                publishers = publishers.filter(founder_name__contains=name)
            elif choice == 'hq_country':
                publishers = publishers.filter(HQ_country__contains=name)
    else:
        publishers = Publisher.objects.all()
    paginator = Paginator(publishers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'publisher/index.html', data)