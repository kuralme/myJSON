''' JavaScript Object Notation '''
import json

with open('exstates.json') as f:
  data = json.load(f)

print(data)

# Print out more readable
for state in data['states']:
  print(state['name'], state['abbrevation'])


# Delete the area codes
for state in data['states']:
  del state['area_codes']

# Make a new file and dump the modified data into it
with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)
  
