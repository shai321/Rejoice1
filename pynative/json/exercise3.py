import json

sampleJson = {"key1": "value1", "key2": "value2", "keys": "value3"}
js=json.dumps(sampleJson,indent=3, separators=(","," = "))
print(js)