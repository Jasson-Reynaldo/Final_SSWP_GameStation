from django.shortcuts import render
from GameList.models.developer import Developer
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from GameList.forms.developer import DeveloperForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import requests

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        developers = Developer.objects.all()
        if name and choice:
            if choice == 'nick_name':
                developers = developers.filter(nick_name__icontains=name)
            elif choice == 'first_name':
                developers = developers.filter(first_name__icontains=name)
            elif choice == 'last_name':
                developers = developers.filter(last_name__icontains=name) 
    else:
        developers = Developer.objects.all()  
    paginator = Paginator(developers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }

    return render(request, 'developer/index.html', context=data)

@login_required
def add_developer(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect(reverse('developer_index'))
    else:
        form = DeveloperForm()

    context = {
        'form': form
    }
    return render(request, 'developer/developer_form.html', context=context)

@login_required
def edit_developer(request, developer_id):
    if request.method == 'POST':
        developer = Developer.objects.get(pk=developer_id)
        form = DeveloperForm(request.POST, instance=developer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('developer_index'))
    else:
        developer = Developer.objects.get(pk=developer_id)
        fields = model_to_dict(developer)
        form = DeveloperForm(initial=fields, instance=developer)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'developer/developer_form.html', context=context)

@login_required
def delete_developer(request, developer_id):
    developer = Developer.objects.get(pk=developer_id)
    if request.method == 'POST':
        developer.delete()
        return HttpResponseRedirect(reverse('developer_index'))
    context = {
        'developer': developer
    }
    return render(request, 'developer/developer_delete.html', context=context)