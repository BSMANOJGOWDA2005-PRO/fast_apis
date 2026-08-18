from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class people(BaseModel):
    name: str
    id: int
    add: str
    
peoples =[
    people(name="manoj",id = 1,add="Mysuru"),
    people(name="siddaraju",id=2,add="basavahalli"),
    people(name="bob",id=3,add = "switzerland")
]
@app.get("/")
def user_name():
    user = input("Enter the user name: ")
    return "wel come to fastapi " + user

@app.get("/people_json")
def get_name():
    return peoples

@app.get("/single_parents")#without path parameter
def name_singel(user_single:str):
    for users in peoples:
        if users.name.lower() == user_single.lower():
            return {
                "id":users.id,
                "name":users.name,
                "add":users.add
            }
    return "the user will not found : "#in fast api not write else statement because it will not work in fast api
            
@app.get("/single_parents/{user_single}")#with path parameter
def name_single(user_single: str):
    for users in peoples:
        if users.name.lower() == user_single.lower():
            return {
                "id": users.id,
                "name": users.name,
                "add": users.add
            }
    return {"message": "The user was not found"}

#-------------------------------------------------------------------------------------------
#post method
@app.post("/people_json")
def add_new_people(new_people:people):
    for users in peoples:
        if users.id == new_people.id:
            return {
                "Message ":" id already exists "
                }
    peoples.append(new_people)
    return {
        "its added successfully the user :{new_people}"
    }
    