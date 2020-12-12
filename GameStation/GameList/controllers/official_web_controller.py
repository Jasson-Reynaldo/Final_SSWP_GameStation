from django.shortcuts import render
from GameList.models.official_web import Official_web
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from GameList.forms.official_web import Official_webForm
from django.contrib.auth.decorators import login_required
import requests

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        official_webs = Official_web.objects.filter(name__icontains=name)
    else:
        official_webs = Official_web.objects.all()  
    data = {
        'official_webs': official_webs,
    }

    return render(request, 'official_web/index.html', context=data)

@login_required
def add_official_web(request):
    if request.method == 'POST':
        form = Official_webForm(request.POST)
        if form.is_valid():
            form.save()  
            return HttpResponseRedirect(reverse('official_web_index'))
    else:
        form = Official_webForm()

    context = {
        'form': form
    }
    return render(request, 'official_web/official_web_form.html', context=context)

@login_required
def edit_official_web(request, official_web_id):
    if request.method == 'POST':
        official_web = Official_web.objects.get(pk=official_web_id)
        form = Official_webForm(request.POST, instance=official_web)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('official_web_index'))
    else:
        official_web = Official_web.objects.get(pk=official_web_id)
        fields = model_to_dict(official_web)
        form = Official_webForm(initial=fields, instance=official_web)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'official_web/official_web_form.html', context=context)

@login_required
def delete_official_web(request, official_web_id):
    official_web = Official_web.objects.get(pk=official_web_id)
    if request.method == 'POST':
        official_web.delete()
        return HttpResponseRedirect(reverse('official_web_index'))
    context = {
        'official_web': official_web,
    }
    return render(request, 'official_web/official_web_delete.html', context=context)