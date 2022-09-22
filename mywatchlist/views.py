from django.shortcuts import render
from mywatchlist.models import MyWatchListItem
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_watchlist(request):
    return render(request, "mywatchlist.html", context)

data_tontonan = MyWatchListItem.objects.all()
context = {
    'list_tontonan': data_tontonan,
    'nama': 'Soraya Sabrina',
    'npm': '2106651061',
}

def show_xml(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchListItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

data_tontonan = MyWatchListItem.objects.all()
contextHTML = {
        'list_tontonan': data_tontonan
    }

def show_html(request):
    return render(request, 'watchedlist.html', contextHTML)

def show_xml_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchListItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")