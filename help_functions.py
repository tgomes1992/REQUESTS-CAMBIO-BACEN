from datetime import datetime, date


def webDateToString(webdate):
    ndate = webdate.strftime("%d/%m/%Y")
    return (ndate)
    


def webStringsToDate(webstring):
    ndate = datetime.strptime(webstring,'%Y-%m-%d')
    return ndate


def formDateAdjustment(formdate):
    ndate = datetime.strptime(formdate,'%Y-%m-%d')
    adjusted_date = ndate.strftime("%d/%m/%Y")
    return adjusted_date
    