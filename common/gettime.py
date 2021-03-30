import time
from datetime import datetime


def timeStamp():
    times=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timeArray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    timeStamp1= int(time.mktime(timeArray))
    return timeStamp1




