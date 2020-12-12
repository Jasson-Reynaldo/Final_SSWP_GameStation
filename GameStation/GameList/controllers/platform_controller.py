from django.shortcuts import render
from GameList.models.platform import Platform
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from GameList.forms.platform import PlatformForm

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

def add_platform(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('platform_index'))
    else:
        form = PlatformForm()

    context = {
        'form': form
    }
    return render(request, 'platform/platform_form.html', context=context)

def edit_platform(request, platform_id):
    if request.method == 'POST':
        platform = Platform.objects.get(pk=platform_id)
        form = PlatformForm(request.POST, instance=platform)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('platform_index'))
    else:
        platform = Platform.objects.get(pk=platform_id)
        fields = model_to_dict(platform)
        form = PlatformForm(initial=fields, instance=platform)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'platform/platform_form.html', context=context)

def delete_platform(request, platform_id):
    platform = Platform.objects.get(pk=platform_id)
    if request.method == 'POST':
        platform.delete()
        return HttpResponseRedirect(reverse('platform_index'))
    context = {
        'platform': platform,
    }
    return render(request, 'platform/platform_delete.html', context=context)