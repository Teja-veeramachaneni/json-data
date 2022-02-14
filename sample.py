import json 
people_string = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "615-555-7164",
            "emails" : ["johnsmith@bogusemail.com","john.smith@work-place.com"],
            "has_licese" : false

        },
        {
            "name" : "John Doe",
            "phone" : "560-555-5153",
            "emails" : null,
            "has_licsense" : true
        }
    ]
}

'''
data = json.loads(people_string)
print(data)
print(type(data['people']))
for person in data['people']:
    del person['phone']
    print(person)
new_str = json.dumps(data, indent = 2)
print(new_str)
new_str1 = json.dumps(data, indent = 2,sort_keys = True)

print(new_str1)

