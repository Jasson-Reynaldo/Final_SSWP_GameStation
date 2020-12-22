from django.shortcuts import render
from django.urls import reverse
from django.forms.models import model_to_dict
from GameList.models.publisher import Publisher
from GameList.forms.publisher import PublisherForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        choice = search['choice']
        publishers = Publisher.objects.all()
        if name and choice:
            if choice == 'name':
                publishers = publishers.filter(name__icontains=name)
            elif choice == 'founder_name':
                publishers = publishers.filter(founder_name__icontains=name)
            elif choice == 'hq_country':
                publishers = publishers.filter(HQ_country__icontains=name)
    else:
        publishers = Publisher.objects.all()
    paginator = Paginator(publishers, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj,
    }
    return render(request, 'publisher/index.html', data)

@login_required
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publisher_index'))
    else:
        form = PublisherForm()

    context = {
        'form': form
    }
    return render(request, 'publisher/publisher_form.html', context=context)

@login_required
def edit_publisher(request, publisher_id):
    if request.method == 'POST':
        publisher = Publisher.objects.get(pk=publisher_id)
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('publisher_index'))
    else:
        publisher = Publisher.objects.get(pk=publisher_id)
        fields = model_to_dict(publisher)
        form = PublisherForm(initial=fields, instance=publisher)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'publisher/publisher_form.html', context=context)

@login_required
def delete_publisher(request, publisher_id):
    publisher = Publisher.objects.get(pk=publisher_id)
    if request.method == 'POST':
        publisher.delete()
        return HttpResponseRedirect(reverse('publisher_index'))
    context = {
        'publisher': publisher,
    }
    return render(request, 'publisher/publisher_delete.html', context=context)    