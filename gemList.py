def getProfitPerGem(corrupted, awakened, altQual, quality, doubleCorrupt, lowConfidence):
    conditions = []
    if not corrupted:
        conditions.append("Vaal")
    if not altQual:
        conditions.append("Anomalous")
        conditions.append("Divergent")
        conditions.append("Phantasmal")

    if not awakened:
        conditions.append("Awakened")

    def key_func(k):
        return k['name']
    import json
    from itertools import groupby
    json_file = validateJson()
 
    data = json.load(json_file)
    data = sorted(data['lines'], key=key_func)
    result = []
    for k, g in groupby(data, key=key_func):
        if any(condition in k for condition in conditions):
            continue

        g = list(g)

        def price_fn(l):
            return l['chaosValue']
        g = sorted(g, key=price_fn)
        min = False
        max = False
        for data in g:
            if not corrupted:  # If filtering out corrupted gems, remove corrupted gem outcomes as well as Vaal gems
                    if 'corrupted' in data:
                        continue
            else:
                    if not doubleCorrupt and isDoubleCorrupt(data):
                        continue
            if not quality:
                    if 'gemQuality' in data:
                        continue
            if not lowConfidence:
                    if data["count"] < 15:
                        continue

            if min == False or max == False:
                    min = data
                    max = data
            chaos = data["chaosValue"]
            if chaos > max["chaosValue"]:
                    max = data
            if chaos < min["chaosValue"]:
                    min = data

        if max == False or "variant" not in max or min == False or "variant" not in min:
            continue

        if max["gemLevel"] == min["gemLevel"]:
            continue
        
        result.append({
                "name": max["name"],
                "profit": round(max["chaosValue"] - min["chaosValue"]),
                "icon": max["icon"],
                "max": max,
                "min": min,
            })

    def profit_fn(l):
            return l['profit']

    result = sorted(result, key=profit_fn, reverse=True)

    return result


def isDoubleCorrupt(gem):
    if 'corrupted' in gem:
        conditions = 0
        if 'gemQuality' in gem:
            if gem["gemQuality"] == 23:
                conditions += 1
        if 'gemLevel' in gem:
            if gem["gemLevel"] == 21:
                conditions += 1
        if "Vaal" in gem["name"]:
            conditions += 1

        return conditions >= 2
    else:
        return False


def validateJson():
    from datetime import datetime
    latest = datetime.today().strftime('%Y%m%d') #Create filename based on date, we use this to check if the file is up to date

    import os
    folder = "./gemDumps/"
    if not os.path.exists(folder): #Create folder if it does not exists, as it is not tracked by git and thus is liable to dissapear
        os.mkdir("gemDumps") 

    for file in os.listdir(folder):
        if latest+(".json") == file:
            return open(folder+file) 

    replaceFile(getJsonFromNinja(),latest)
    return validateJson()

def getJsonFromNinja():
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    url = "https://poe.ninja/api/data/itemoverview?league=Kalandra&type=SkillGem"
    try:
        req = Request(
            url=url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        gemList = urlopen(req).read().decode().replace('\n', '')
    except HTTPError as e:
        print("Error occured!")
        print(e)

    return (gemList)

def replaceFile(json, fileName):
    import os
    for file in os.listdir("./gemDumps/"):
        if file.endswith(".json"):
            os.remove(file)
    file = open("./gemDumps/"+fileName+".json", "w")
    file.write(json)
    file.close
