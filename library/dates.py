import datetime


def getDates(n=10):
    base = datetime.datetime.fromisoformat("2019-11-01")
    date_list = [(base + datetime.timedelta(days=x)) for x in range(n)]
    return date_list