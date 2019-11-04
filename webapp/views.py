from django.shortcuts import render
from django.http import HttpResponse

from library.words import *
from library.points import *
from library.maps import *
from library.htmls import *
from library.dates import *

# Create your views here.
def home(request):
    return HttpResponse("<a href='/html?n=30'>Go here</a>")

def maplocal(request):
    lon = float(request.GET['lon'])
    lat = float(request.GET['lat'])
    return getLocalMapResponse(Point(lon,lat))

def mapoverview(request):
    lon = float(request.GET['lon'])
    lat = float(request.GET['lat'])

    #TODO: Change
    return getLocalMapResponse(Point(lon,lat))

def html(request):
    n = int(request.GET['n'])
    print("--Generating dates")
    dates = getDates(n)

    print("--Generating words")
    words = getWords(n)

    print("-- Reading city polygon")
    city = getPolygon()

    print("-- Generating points")
    points = getPoints(city, n)
    
    print("--Generating html")
    html = generateHtml(points, words, dates)
    response = HttpResponse(html)
    return response