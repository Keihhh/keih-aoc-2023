import re
import itertools 

with open('day2\input.txt', encoding='utf-8') as f:
    data = f.read()
#Part 1
def possible_combinations_idsum(data):
    data = data.replace('\n',':')
    data = re.sub('Game \d','',data)
    datalist = data.split(':')
    cslist = [re.findall('(\d{2} red|\d{2} blue|\d{2} green|\d green|\d blue|\d red)', lines) for lines in datalist]
    cslist = list(filter(None, cslist))
    cslist = list(enumerate(cslist,1))
    
    possible_ids = 0
    notpossiblefilter = re.compile('[2-9][0-9] red|1[3-9] red|[2-9][0-9] blue|1[5-9] blue|[2-9][0-9] green|1[4-9] green')
    for games, cubes in cslist:
        newlist = list(filter(notpossiblefilter.match, cubes))
        if newlist == []:
            possible_ids +=games
    return possible_ids

print(possible_combinations_idsum(data))

#Part 2
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
        greenlist = list(filter(greenfilter.match, cubes))
        greenlist = str(greenlist)
        greenlist = greenlist.replace('[','').replace(']','').replace("'",'').replace(',','')
        greenlist = greenlist.split()
        greenlist = list(filter(numbersfilter.match, greenlist))
        greenlist = [int(n) for n in greenlist]

        redlist = list(filter(redfilter.match, cubes))
        redlist = str(redlist)
        redlist = redlist.replace('[','').replace(']','').replace("'",'').replace(',','')
        redlist = redlist.split()
        redlist = list(filter(numbersfilter.match, redlist))
        redlist = [int(n) for n in redlist]

        bluelist = list(filter(bluefilter.match, cubes))
        bluelist = str(bluelist)
        bluelist = bluelist.replace('[','').replace(']','').replace("'",'').replace(',','')
        bluelist = bluelist.split()
        bluelist = list(filter(numbersfilter.match, bluelist))
        bluelist = [int(n) for n in bluelist]

        multiplier = max(greenlist) * max(redlist) *max(bluelist)
        sum += multiplier

    return sum

print(sumofpowers_sets(data))