from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import QueryForm
from .management.commands import craigslist_toronto_scraper


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # get data in cleaned format
            search = form.cleaned_data['search']
            category = form.cleaned_data['category']
            search_results = run_search(search, category)
            return JsonResponse(search_results, safe=False, json_dumps_params={'indent': 2})

    form = QueryForm()
    return render(request, 'home.html', {'form': form})


def run_search(search_text, category):
    return craigslist_toronto_scraper.Command().handle(query=search_text, category=category)
