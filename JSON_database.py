import json 


shipments = {}


## Load from .json file

with open("shipments.json") as json_file:
    data = json.load(json_file)

    # Get shipment by id:
    for shipment in data:
        if shipment ["id"] == "12701":
            print(shipment)

    # Map as dictionary
    for value in data:
        shipments[value["id"]] = value

print(shipments)

## Save changes to .json file
def save(): 
    with open("shipments.json", "w") as json_file:
        json.dump(
            # Convert to list of shipments
           list(shipments.values()),
           json_file)
       #json.dump(list(shipments.values()), json_file, indent=4)
       #pass