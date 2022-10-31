import json
j = '{"X":"value1", "Y":"value2", "Z":[{"A":"value3", "B":"value4"}]}'
k = json.loads(j)
assert k["Z"][0]["A"] == "value3"