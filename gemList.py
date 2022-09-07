def getProfitPerGem():
    conditions = ["Vaal","Anomalous","Divergent","Phantasmal"]
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
                if 'corrupted' not in data:
                    
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
                else:
                    continue
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
