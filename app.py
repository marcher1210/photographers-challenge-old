from flask import Flask, request

from library.words import *
from library.points import *
from library.maps import *
from library.htmls import *
from library.dates import *

import datetime 


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from photo project!"


@app.route("/map/")
def map():
    return getLocalMap(Point(55.423, 12.567))

gUrl = r"http://www.google.com/maps/place/{0},{1}"

@app.route("/html/")
def html():
    n = request.args.get('n', default = 30, type = int)

    print("--Generating dates")
    dates = getDates(n)

    print("--Generating words")
    words = getWords(n)

    print("-- Reading city polygon")
    city = getPolygon()

    print("-- Generating points")
    points = getPoints(city, n)
    
    print("--Generating html")
    return generateHtml(points, words, dates)
    generateHtmlMeta(points, words, dates)

    print("-- Retrieving overview map")
    x1, y1, x2, y2 = city.bounds
    map = getMap(y1, x1, y2, x2)
    
    print("-- Drawing all points on map")
    drawOnMapAndSave(map, points, "html/maps/map_all.png")

    data = []
    print("")
    for i, p in enumerate(points):
        print("-- Point ","{:02d}".format(i)," of ",n)
        #print("When: ",dates[i])
        #print("What: ", words[i])
        #print("Where: "+gUrl.format(p.y, p.x))
        print("     Overview map...")
        drawPoint(map, p, i)

        print("     Local map...")
        drawLocalMap(p, i)
        data.append({
            "date": dates[i].strftime("%d-%m-%Y"),
            "word": words[i],
            "point": "({0},{1})".format(points[i].x, points[i].y)
        })
    f = open("html/data.txt", mode='w')
    f.write(str(data))
    f.close()


