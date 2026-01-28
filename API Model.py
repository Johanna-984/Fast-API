from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from typing import Callable, Any
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate


app = FastAPI()


shipments = {
    12701: {"weight": 0.6, "content": "glassware", "status": "placed", "destination": 10001},
    12702: {"weight": 2.3, "content": "books", "status": "shipped", "destination": 10002},
    12703: {"weight": 1.1, "content": "electronics", "status": "delivered", "destination": 10003},
    12704: {"weight": 3.5, "content": "furniture", "status": "in transit", "destination": 10004},
    12705: {"weight": 0.9, "content": "clothing", "status": "returned", "destination": 10005},
    12706: {"weight": 4.0, "content": "appliances", "status": "processing", "destination": 10006},
    12707: {"weight": 1.8, "content": "toys", "status": "placed", "destination": 10007},
}


@app.get("/shipment", response_model= ShipmentRead)

def get_shipment(id: int):

#Check for shipment with given id
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id doesn´t exist!"
        )
    
    return shipments[id]


@app.post("/shipment")
def submint_shipment(shipment: ShipmentCreate
    #content: str, weight: float, destination: int
    ) -> dict[str, int]:
    # Generate new id
    new_id = max(shipments.keys()) + 1
    # Add to shipments dict
    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "destination": shipment.destination,
        "status": "placed",
    }
    # Return id for later use
    return {"id": new_id}


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, body: ShipmentUpdate):
    # Update data given fields
    shipments[id].update(body)
    return shipments[id]


@app.put("/shipment")
def shipment_update(
    id: int, 
    content: str,
    weight: float, 
    status: str) -> dict[str, Any]:

    shipments[id]= {
        "content": content,
        "weight": weight,
        "status": status,
    } 
    return shipments[id]


@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> Any:
    return{
        field: shipments[id][field]
    }


@app.delete("/shipment")
def delete_shipment(id:int) -> dict[str, str]:
    shipments.pop(id)
    return{"detail": f"Shipment with id {id} is deleted!"}


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )