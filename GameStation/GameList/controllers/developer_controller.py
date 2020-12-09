from django.shortcuts import render
from GameList.models.developer import Developer

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        developers = Developer.objects.all()
        if name and choice:
            if choice == 'first_name':
                developers = developers.filter(first_name__contains=name)
            elif choice == 'last_name':
                developers = developers.filter(last_name__contains=name)
    else:
        developers = Developer.objects.all()  
    data = {
        'developers': developers,
    }

    return render(request, 'developer/index.html', context=data)