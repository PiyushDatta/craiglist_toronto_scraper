from django.shortcuts import render
from django.http import HttpResponse
from .forms import QueryForm


def index(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # get data in cleaned format
            search = form.cleaned_data['search']
            category = form.cleaned_data['category']
            print(search, category)

    form = QueryForm()
    return render(request, 'home.html', {'form': form})


def run_search(request):
    search_query = request.GET.get['query']
