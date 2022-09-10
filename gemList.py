def getProfitPerGem(corrupted,awakened,altQual,quality,doubleCorrupt,lowConfidence):
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
    with open('itemoverview.json') as json_file:
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
                if not corrupted: #If filtering out corrupted gems, remove corrupted gem outcomes as well as Vaal gems
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
                    
            if max == False or "variant" not in max:
                return "max is not set"
            if min == False or "variant" not in min:
                return "min is not set"
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
