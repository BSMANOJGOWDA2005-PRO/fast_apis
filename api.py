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
                "message": "ID already exists"
            }
    peoples.append(new_people)
    return {
        "message": f"User added successfully: {new_people.name}"
    }
#-------------------------------------------------------------------------------------------
@app.put("/people_json")
def update_people(id: int , people_add: people):
    for i in range(len(peoples)):
        if peoples[i].id == id:
            peoples[i]=people_add
            return {
                 "message":"the user is updated successfully"
            }
    return {
        "message":"the user is not found"   
    }
    
#-------------------------------------------------------------------------------------------

@app.delete("/people_json")
def delete_people(id: int):
    for i in range(0,len(peoples)):
        if peoples[i].id == id:
            delet = peoples.pop(i)
            return {
                "message": "User deleted successfully",
                "deleted_user": delet
            }
    return {
        "message": "User not found"
    }
#---------------------------------------------------------------------------------------------------
"""
-> To create the venv(virtual environment) in the project folder
*   python -m venv myenv //py -m venv
*  myenv\Scripts\activate //myenv\Scripts\activate.bat
*  deactivate //deactivate.bat
*fastapi is a modern, fast (high-performance),
    web framework for building APIs using py
    
* uvicorn is a lightning-fast ASGI server implementation, 
ASGI(Asynchronous Server Gateway Interface) its web server for fastapi


-> To install the fastapi and uvicorn in the venv
*   pip install fastapi uvicorn
*   pip install pydantic (pydantic is used for data validation)
*   py -m uvicorn api(file):app(varible we assigned "app = FastAPI()") --reload 

"""
#---------------------------------------------------------------------------------------------------
"""
-> gunicorn  are used to the flask and django

"""