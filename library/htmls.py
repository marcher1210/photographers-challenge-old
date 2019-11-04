from random import *
import datetime

def calenderCoordinate(date):
    y = date.isocalendar()[1]-44
    x = date.isocalendar()[2]-1
    return y,x

def generateHtml(points, words, dates):
    html = ""

    rnd = Random()

    pointHtmlList = []
    for i, point in enumerate(points):
        word=words[i]
        date=dates[i]
        y,x = calenderCoordinate(date)
        top = 42 + y * 11.5
        left= 3  + x * 14
        pointHtmlList.append(
            ''' 
    <div class="page">
    <h1>{datestr}</h1>
    <p>&nbsp;</p>
    <div class="item">
        <div class="polaroid">
        <div class="img word">
            <div class="text" style="transform: rotate({rotate1}deg);">{word}</div>
        </div>
        <div class="caption">What</div>
        </div>
    </div>

    <div class="item">
    <div class="polaroid">
        <div class="img calendar" style="position:relative;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Red_X_Freehand.svg"
            style="position: absolute;
            width: 10%;
            height: 10%;
            left: {left}%;
            top: {top}%;"/>
            <div class="text">{datestr}</div>
        </div>
        <div class="caption">When</div>
        </div>
    </div>

    <div class="item">
        <div class="polaroid"><img src="/mapoverview?lon={point.x}&lat={point.y}">
        <div class="caption">Where</div>
        <div class="smallcaption">
        <a href="http://www.google.com/maps/place/{point.y},{point.x}" target="_blank">
        ({point.x},{point.y})
        </a>
        </div>
        </div>
    </div>

    <div class="item">
        <div class="polaroid"><img src="/maplocal?lon={point.x}&lat={point.y}">
        <div class="caption">Where</div>
        <div class="smallcaption">
        <a href="http://www.google.com/maps/place/{point.y},{point.x}" target="_blank">
        ({point.x},{point.y})
        </a>
        </div>
        </div>
    </div>

    <div class="notes">
        <div class="caption">Notes</div>
    </div>
    </div>
            '''.format(i=i, point=point, word=word, datestr=date.strftime("%d-%m-%Y"), rotate1=rnd.randint(-30,30), rotate2=rnd.randint(-30,30), left=left, top=top)
        )


    # Insert newlines between every element, with a * prepended
    inserted_list = '\n'.join(pointHtmlList)

    html = '''<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"> 
        <meta charset="utf-8">
        <title>Photo project</title>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <style>
            div.page{
                page-break-after: always;
                margin: 3rem;
                text-align: center;
            }
            * {
            box-sizing: border-box;
            }

            .wrapper {
            width: 30cm;
            padding: 0 2rem;
            text-align: center;
            }
            .polaroid {
            background: #FFF;
            padding: 1rem;
            box-shadow: 0 0.2rem 1.2rem rgba(0,0,0,0.2);
            }
            /*@media print {
                .polaroid {
                    -webkit-filter: drop-shadow(0 0.2rem 1.2rem rgba(0,0,0,0.2));
                    text-shadow: 0 0.2rem 1.2rem rgba(0,0,0,0.2);
                }
            }*/
            .polaroid > img,
            .polaroid > .img {
            width: 11cm;
            height: 11cm;
            }
            .polaroid > .img {
            background-size: 100%%;
            background-repeat: no-repeat;
            background-position: bottom;

            }
            .img.word {
            background-color: #ccc;
            background-blend-mode: overlay;
            background-image: url('https://ctl.s6img.com/society6/img/gb6wISBRFuxYSlwPPZJjiLWWb-o/w_700/leggings/swatch/~artwork,fw_7500,fh_9000,iw_7500,ih_9000/s6-0090/a/35220406_6915155/~~/dark-sepia-backgroundpattern-twl-leggings.jpg');

            }
            .img.calendar {
                background-image: url('https://blankcalendarpages.com/printable_calendar/monday1/November-2019-calendar-monday-start1.jpg');
            }
            .polaroid > .img.word > .text
            {
                padding-top: 40%%;
                font-size: 3rem;
            }
            .polaroid > .img.calendar > .text
            {
                padding-top: 5%%;
                font-size: 2rem;
            }
            .caption {
            font-size: 1.8rem;
            text-align: center;
            line-height: 2em;
            }
            .smallcaption {
            font-size: 0.9rem;
            text-align: center;
            line-height: 1em;
            }
            .item,
            .notes {
            display: inline-block;
            margin: 1rem;
            border: 1px solid #666;
            }
            .notes {
                width: 24.8cm;
                height: 8cm;

            }
        </style>
    </head>
    <body>
    <div class="wrapper">
    <div class="page">
        <h1>Photo project</h1>
        <div style="height:20cm;">&nbsp;</div>
    </div>
    %s
    </div>
    </body>
    </html>''' %(inserted_list)
    #f = open("html/index.html", "w")
    #f.write(html)
    #f.close()
    return html

def generateHtmlMeta(points, words, dates):
    html = ""

    pointHtmlList = []
    for i, point in enumerate(points):
        word=words[i]
        date=dates[i]
        pointHtmlList.append(
            ''' 
    <div class="row">
        <div class="col-md">
            <a href="http://www.google.com/maps/place/{point.y},{point.x}" target="_blank">
            {datestr}
            </a>
        </div>
    </div>
            '''.format(i=i, point=point, word=word, datestr=date.strftime("%d-%m-%Y"))
        )


    # Insert newlines between every element, with a * prepended
    inserted_list = '\n'.join(pointHtmlList)

    html = '''<html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8"> 
        <meta charset="utf-8">
        <title>Google Links</title>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        
    </head>
    <body>
    <div class="container">
    <h1>Google Links</h1>
    %s
    </div>
    </body>
    </html>''' %(inserted_list)
    f = open("html/googlelinks.html", "w")
    f.write(html)
    f.close()
    return html

if __name__ == "__main__":
    for i in getDates(30):
        y,x = calenderCoordinate(i)
        print("{0}: y:{1} x:{2}".format(i.isocalendar(),y,x))