import json, math

def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x
def plural(n, word, form=None): return str(jsnum(n)) + " " + (word if n == 1 else (form or word + "s"))
def fmt(x): return str(jsnum(x))
def round1(x): return jsnum(math.floor(x * 10 + 0.5) / 10)

RUNOFF_COEF = 0.9
BED_PCT = 15
MULCH_CM = 8
BAG_L = 50

def catch_plan(areaM2, rainCm):
    if not (areaM2 > 0) or not (rainCm > 0):
        return {"error": "the area and the rain must be positive"}
    liters = round1(areaM2 * rainCm * 10 * RUNOFF_COEF)
    if liters <= 500: verdict = "barrel scale"
    elif liters <= 3000: verdict = "garden scale"
    else: verdict = "swale territory"
    return {"liters": liters, "verdict": verdict}

def bed_plan(areaM2):
    if not (areaM2 > 0):
        return {"error": "the area must be positive"}
    bed = round1(areaM2 * BED_PCT / 100)
    if bed <= 4: verdict = "a planter box"
    elif bed <= 15: verdict = "a weekend dig"
    else: verdict = "a landscaper's job"
    return {"bed": bed, "verdict": verdict}

def mulch_plan(bedM2):
    if not (bedM2 > 0):
        return {"error": "the bed must be positive"}
    liters = round1(bedM2 * MULCH_CM * 10)
    bags = math.ceil(liters / BAG_L)
    if bags <= 4: verdict = "a car-trunk haul"
    elif bags <= 16: verdict = "a few trips"
    else: verdict = "a delivery load"
    return {"liters": liters, "bags": bags, "verdict": verdict}

def render_catch(r, areaM2, rainCm):
    return ("A " + fmt(rainCm) + " cm rain on your " + fmt(areaM2) + " m2 roof sends " + fmt(r["liters"])
            + " L your way at a labeled " + fmt(RUNOFF_COEF) + " runoff coefficient - " + r["verdict"] + ".")

def render_bed(r, areaM2):
    return ("Your " + fmt(areaM2) + " m2 roof at a labeled " + fmt(BED_PCT) + " percent rule names a " + fmt(r["bed"])
            + " m2 bed - " + r["verdict"] + ".")

def render_mulch(r, bedM2):
    return ("Your " + fmt(bedM2) + " m2 bed at a labeled " + fmt(MULCH_CM) + " cm of mulch asks " + fmt(r["liters"])
            + " L - " + plural(r["bags"], "bag") + " of labeled " + fmt(BAG_L) + " L, " + r["verdict"] + ".")

cases = []
def add(fn, f, rf, args):
    r = f(*args)
    c = {"fn": fn, "args": args, "result": r}
    if "error" not in r: c["render"] = rf(r, *args)
    cases.append(c)

for a in [[100,5],[40,2],[20,1],[60,3],[80,4],[30,2],[10,2],[120,6],[0,5],[100,0]]:
    add("catchPlan", catch_plan, render_catch, a)
for a in [[100],[30],[20],[200],[60],[150],[10],[250],[0],[80]]:
    add("bedPlan", bed_plan, render_bed, a)
for a in [[15],[10],[40],[60],[100],[110],[5],[200],[0],[25]]:
    add("mulchPlan", mulch_plan, render_mulch, a)
json.dump(cases, open("expected.json", "w"), separators=(",", ":"))
print(len(cases), "cases")
