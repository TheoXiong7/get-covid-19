import requests as r
import json

def gltotal():
    ac_req = r.get("https://corona.lmao.ninja/v2/all")
    all_cases = json.loads(ac_req.text)
    return all_cases["cases"]

def glactive():
    ac_req = r.get("https://corona.lmao.ninja/v2/all")
    all_cases = json.loads(ac_req.text)
    return all_cases["active"]

def ustotal():
    us_req = r.get("https://corona.lmao.ninja/v2/countries")
    l = json.loads(us_req.text)
    if l[207]["country"] == "USA":
        return l[207]["cases"]
    else:
        return "Error"

def usactive():
    us_req = r.get("https://corona.lmao.ninja/v2/countries")
    l = json.loads(us_req.text)
    #print(l[207])
    if l[207]["country"] == "USA":
        return l[207]["active"]
    else:
        return "Error"

print(usactive())