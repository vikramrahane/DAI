Dict = { 
 "name": "Kelly", 
 "age":25, 
 "salary": 8000, 
 "city": "New york" 
} 
val=Dict.get("city",-1)
if val!=-1:
    Dict.pop("city")
    Dict["Location"]=val
print(Dict)