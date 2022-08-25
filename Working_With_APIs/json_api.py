import json

# Working with JSON and APIs

#Reading JSON with the loads() Function

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# Writing JSON with the dumps() Function
# This translate python value into a string of JSON-fromatted data

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)