import json
import urllib.parse
import urllib.request

# API Endpoint definition
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# Prompt user for location input
address = input("Enter location: ")
if len(address) < 1:
    address = "Irkutsk State University"

# Encode parameters including location query and API key
parms = dict()
parms["q"] = address
parms["key"] = 42
url = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except Exception:
    js = None

if not js or "features" not in js or len(js["features"]) == 0:
    print("=== Failure To Retrieve ===")
    print(data)
else:
    # Retrieve the first plus_code from the properties of the first feature
    plus_code = js["features"][0]["properties"]["plus_code"]
    print("Plus code", plus_code)