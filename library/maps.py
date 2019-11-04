import smopy
from io import StringIO

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

overview_fn = "html/maps/map_{:02d}_overview.png"
local_fn =    "html/maps/map_{:02d}_zoom.png"

localMapRadius=0.005


def getMap(y1, x1, y2, x2):
    map = smopy.Map((y1, x1, y2, x2), tileserver="http://tile.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png", tilesize=512, maxtiles=16)
    return map

def drawPoint(map, p, counter):
    fn = overview_fn.format(counter)
    #print("Draw ",fn)
    drawOnMapAndSave(map, [p], fn)

def drawLocalMap(p, counter):
    fn = local_fn.format(counter)
    #print("Draw ",fn)

    x1 = p.x - localMapRadius
    y1 = p.y - localMapRadius/2
    x2 = p.x + localMapRadius
    y2 = p.y + localMapRadius/2

    map = getMap(y1, x1, y2, x2)

    drawOnMapAndSave(map, [p], fn)

def drawOnMapAndSave(map, ps, fn):
    ax = map.show_mpl(figsize=(5,5), dpi=300)
    for p in ps:
        x, y = map.to_pixels(p.y, p.x)
        ax.plot(x, y, 'or', ms=5, mew=1, alpha=0.35)
    plt.savefig(fn)
    plt.close('all')


def getLocalMap(p):

    x1 = p.x - localMapRadius
    y1 = p.y - localMapRadius/2
    x2 = p.x + localMapRadius
    y2 = p.y + localMapRadius/2

    map = getMap(y1, x1, y2, x2)

    #Plot
    ax = map.show_mpl(figsize=(5,5), dpi=300)
    x, y = map.to_pixels(p.y, p.x)
    ax.plot(x, y, 'or', ms=5, mew=1, alpha=0.35)
    canvas.savefig()
    plt.savefig()

    return response
    
