import json

# Read the JSON file
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Update the JSON data
ex5[2]['batters']['batter'].append({"id":"1003","type":"Coffee"})

# Write the updated JSON data back to the file
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)