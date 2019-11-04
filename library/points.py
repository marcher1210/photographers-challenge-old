import geopandas as gpd
from shapely.geometry import Point, Polygon
import random as rnd

gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

def getPolygon(fp = "assets/cph.kml"):
    polys = gpd.read_file(fp, driver='KML')
    city = polys.loc[0, 'geometry']

    return city

def getPoints(poly, n = 10):
    i = 0
    x1, y1, x2, y2 = poly.bounds

    ps = []

    while i < n:
        p = Point(round(rnd.uniform(x1, x2), 5), round(rnd.uniform(y1,y2),5))
        if(p.within(poly)):
            ps.append(p)
            i += 1
    return ps