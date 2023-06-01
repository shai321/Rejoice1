import json
json1="""[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

js=[]
try:
   js=json.loads(json1)
except Exception as e:
   print(e)

js1=[i.get("name") for i in js]
print(js1)