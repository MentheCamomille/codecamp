import json
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient

app = FastAPI()

client = MongoClient('mongodb://localhost:27017/')
db = client['ageimpulse']
devices_collection = db['devices']
clients_collection = db['clients']
users_collection = db['users']

class IoTDevice(BaseModel):
    id: int
    name: str
    hw_version: str
    fw_version: str
    lot: str
    serial_number: str
    client_id: int

class Client(BaseModel):
    id: int
    name: str

class User(BaseModel):
    id: int
    name: str
    email: str

def load_json(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

initial_devices = load_json("../json/iot.json")
initial_clients = load_json("../json/client.json")
initial_users = load_json("../json/users.json")

@app.get('/')
def read_root():
    return{"Bienvenue sur l'api ageimpulse"}

@app.post("/devices/", response_model=IoTDevice)
def create_device(device: IoTDevice):
    result = devices_collection.insert_one(device.dict())
    device.id = result.inserted_id
    return device

@app.get("/devices/", response_model=List[IoTDevice])
def get_devices():
    devices = list(devices_collection.find())
    return devices

@app.post("/clients/", response_model=Client)
def create_client(client: Client):
    result = clients_collection.insert_one(client.dict())
    client.id = result.inserted_id
    return client

@app.get("/clients/", response_model=List[Client])
def get_clients():
    clients = list(clients_collection.find())
    return clients

@app.post("/users/", response_model=User)
def create_user(user: User):
    result = users_collection.insert_one(user.dict())
    user.id = result.inserted_id
    return user

@app.get("/users/", response_model=List[User])
def get_users():
    users = list(users_collection.find())
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)