"""
This links to our home.html file. This is what the user sees.
"""

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import QueryForm
from .management.commands import craigslist_toronto_scraper


def index(request):
    """
    Shows json data to home.html and also shows our form variable
    :param request: HttpRequest object
    :return: JsonResponse object
    """
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # get data in cleaned format
            search = form.cleaned_data['search']
            category = form.cleaned_data['category']
            search_results = run_search(search, category)
            # Send user to another page, same address, with json response that is formatted
            return JsonResponse(search_results, safe=False, json_dumps_params={'indent': 2})

    form = QueryForm()
    return render(request, 'home.html', {'form': form})


def run_search(search_text, category):
    """
    Run our magic search
    :param search_text: String
    :param category: String
    :return: List[{dict}]
    """
    return craigslist_toronto_scraper.Command().handle(query=search_text, category=category)
