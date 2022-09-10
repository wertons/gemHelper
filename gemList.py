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
    formattedresult = ""
    for k, g in groupby(data, key=key_func):
        if any(condition in k for condition in conditions):
            continue
        formattedresult += "\n <br> " + k

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
            formattedresult += "\n   <br>  " + \
                    (data["variant"]) + " | " + str(chaos) + " Chaos"

        if max == False or "variant" not in max or min == False or "variant" not in min:
                continue

        formattedresult += "\n   <br>  max: " + \
                max["variant"] + " | min: " + min["variant"] + "<br> profit is " + \
                str(max["chaosValue"] - min["chaosValue"]) + " <br>"
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
    latest = datetime.today().strftime('%Y%m%d')
    import os
    exists = False
    folder = "./gemDumps/"
    for file in os.listdir(folder):

        if latest in file:
            exists = True
            return open(folder+file) 
    if not exists:
        json = getJsonFromNinja()
        replaceFile(json,latest)
        validateJson()

def getJsonFromNinja():
    from urllib.request import Request, urlopen
    import json
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
    for file in os.listdir("."):
        if file.endswith(".json"):
            os.remove(file)
    file = open("./gemDumps/"+fileName+".json", "w")
    file.write(json)
    file.close
