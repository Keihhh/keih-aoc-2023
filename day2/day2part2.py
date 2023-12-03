import re
import itertools 

with open('day2\input.txt', encoding='utf-8') as f:
    data = f.read()

def sumofpowers_sets(data):
    data = data.replace('\n',':')
    data = re.sub('Game \d','',data)
    datalist = data.split(':')
    cslist = [re.findall('(\d{2} red|\d{2} blue|\d{2} green|\d green|\d blue|\d red)', i) for i in datalist]
    cslist = list(filter(None, cslist))
    #cslist = list(enumerate(cslist,1))

    numbersfilter = re.compile('\d{2}|\d')
    greenfilter = re.compile('\d{2} green|\d green')
    redfilter = re.compile('\d{2} red|\d red')
    bluefilter = re.compile('\d{2} blue|\d blue')

    sum = 0

    for cubes in cslist:
        #print(cubes)
        greenlist = list(filter(greenfilter.match, cubes))
        greenlist = str(greenlist)
        greenlist = greenlist.replace('[','').replace(']','').replace("'",'').replace(',','')
        greenlist = greenlist.split()
        greenlist = list(filter(numbersfilter.match, greenlist))
        greenlist = [int(n) for n in greenlist]
        #print(greenlist)


        redlist = list(filter(redfilter.match, cubes))
        redlist = str(redlist)
        redlist = redlist.replace('[','').replace(']','').replace("'",'').replace(',','')
        redlist = redlist.split()
        redlist = list(filter(numbersfilter.match, redlist))
        redlist = [int(n) for n in redlist]
        #print(redlist)

        bluelist = list(filter(bluefilter.match, cubes))
        bluelist = str(bluelist)
        bluelist = bluelist.replace('[','').replace(']','').replace("'",'').replace(',','')
        bluelist = bluelist.split()
        bluelist = list(filter(numbersfilter.match, bluelist))
        bluelist = [int(n) for n in bluelist]
        #print(bluelist)

        multiplier = max(greenlist) * max(redlist) *max(bluelist)
        sum += multiplier
        #print(max(greenlist))
        #print(max(redlist))
        #print(max(bluelist))
        #print(multiplier)
    return sum

print(sumofpowers_sets(data))
        