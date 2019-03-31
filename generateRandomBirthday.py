import random
import time


# input -> number of birthday to be generated
# output -> a list of randomly generated birthday
# with the format dd/mm/yyyy

def strTimeRandom(start, end, format):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + random.random() * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def generateBirthdays(n):
    birthdays = []
    for i in range(n):
        birthdays.append(strTimeRandom('1/1/2010', '1/1/2018', '%m/%d/%Y'))
    return birthdays


randomBirthday = generateBirthdays(10)

print(type(randomBirthday))
print(randomBirthday)
