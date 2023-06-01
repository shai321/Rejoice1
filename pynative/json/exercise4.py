import json

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
with open("sampleJson.json", "w") as f:
    json.dump(sampleJson, f, indent=3, sort_keys=True)
print("Done writing JSON data into a file")

