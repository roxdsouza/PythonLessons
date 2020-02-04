import json
str = ""

with open("c:\\temp\\test.json") as data_file:
    data = json.load(data_file)
    for p in data:
        for key in sorted(p.keys()):
            if p[key] == 'Old Fashioned':
                allList = p['batters']['batter']
                for i in allList:
                    str += i['type'] + "|\n"

if not str:
    print "Nothing Found!"
else:
    print str