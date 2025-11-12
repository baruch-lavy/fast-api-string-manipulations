import json
from fastapi import FastAPI,Body,HTTPException
from pydantic import BaseModel,Field

app = FastAPI()

class Item(BaseModel):
    name:str
    price:int
    
class ItemToUpdate(BaseModel):
    name:str
    price:int
    
class ItemToDelete(BaseModel):
    name:str = Field(
        min_length=1,
        max_length=50,
        description="the item to delete"
    )


def load_data(path):
    try:
        with open(path,'r') as f:
            data = json.load(f)
            
    except (json.JSONDecodeError):
        data = []
        
    return data
         
def save_data(path,data_to_save,is_update=False):
    if not is_update:
        data = load_data(path)
        data.append(data_to_save)
    else:
        data = data_to_save
    with open('data.json','w') as f:
        json.dump(data,f,indent=4)

# routes

@app.get("/items")
def return_items():
    data = load_data()
    return data

# option 1
# @app.post("/item/")
# def update_data(item:dict = Body()):
#     item = item
#     save_data('item.json',item)
#     return item

# # option 2
# @app.post("/items/")
# def update_data(y:dict):
#     data_to_save = y.get('name')
    # save_data('data.json',data_to_save)
    # return "data saved successfully"

# option 3 : recommended
@app.post("/items/")
def update_data(item:Item):
    data_to_save = {item.name:item.price}
    save_data('data.json',data_to_save,True)
    return "data saved successfully"

def item_in_data(data,name):
    for i in range(len(data)):
        if len(data) == 1:
            return name in data[0]
        return name in data[i] or item_in_data(data[:i],name)

 
@app.put("/update-item/{item_name}")
def update_data(item_name:str,item:ItemToUpdate):
    data = load_data("data.json")
    if not item_in_data(data,item_name):
        return HTTPException(status_code=400,detail="item not found")
    for product in data:
        if item.name in product:
            product[item.name] = item.price
    save_data("data.json",data,True)
    return data

@app.delete("/item-to-delete/")
def delete_item(item:ItemToDelete):
    data = load_data("data.json")
    if not item_in_data(data,item.name):
        return HTTPException(status_code=400,detail="item not found")
    for product in data:
        if item.name in product:
            del product[item.name]
    save_data("data.json",data,True)
    return data