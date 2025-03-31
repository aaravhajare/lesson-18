import time
import random

def randomdate(start,end) :
    randomgenrator = random.random()
    dateformat = "%d/%m/%Y"

    start = time.mktime(time.strptime(start,dateformat))
    end = time.mktime(time.strptime(end,dateformat))

    randomtime = start + randomgenrator * (end - start)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate

print(randomdate("01/01/2000" , "01/01/2025"))