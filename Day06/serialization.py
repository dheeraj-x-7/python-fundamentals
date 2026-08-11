l = [1,2,3,4,5,6,7]
student = {"name":"Peter Parker",
           "age":21,
           "Category": "SuperHero",
           "Role":"SpiderMan",
           "Friends": ['Iron man', 'Hulk','Thor','Captain America','Dr. Strange'],
           "Roll Num": 3000}
import json
with open('Sample2.txt','w') as f:
    json.dump(student,f,indent=4)
   # json.dump(l,f)

with open('Sample2.txt','r') as f:
    d = json.load(f)
    print(d)