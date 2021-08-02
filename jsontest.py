import json

# a simple json object
peoplestring = '''
{
  "people" =
  [
	{
	"name": "ege",
	"phone": "123123",
	"emails": ["egekural1992","krlmeigen"],
	"age": "29"
	},
	{
	"name": "mege",
	"phone": "12312223",
	"emails": ["xxx","yyy"],
	"age": "29"
	}
  ]
}
'''
# json to python dictionary
# https://docs.python.org/3/library/json.html#encoders-and-decoders
data = json.loads(peoplestring)


print(type(data))
print(data)



# print names of the peoples
for person in data['people']:
	print(person['name'])



# Delete phones from each people	
for person in data['people']:
	del person['phone']

# Print out in easy readble form
new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)