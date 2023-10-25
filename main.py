from fastapi import FastAPI, Depends
from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
import models
import schemas

#create DB based on the engine passed
Base.metadata.create_all(engine)

app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

tasksDB = {
    1:{'task':'task 1'},
    2:{'task':'task 2'},
    3:{'task':'task 3'},
}

# @app.get("/")
# def getItems():
#     return tasksDB

@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()    
    return items


# #to pass a parameter
# @app.get("/{id}")
# def getItemById(id:int):
#     return tasksDB.get(id)


# @app.post("/")
# def addItem(item:schemas.Item):
#     newId = len(tasksDB.keys()) + 1
#     tasksDB[newId] = {"task":item.task}
#     return tasksDB


@app.post("/")
#schemas.Item : its pydantic model 
#received from the request
#models.Item: its DB model. assign the value to it and save in DB
def addItem(item:schemas.Item, session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

@app.delete("/{id}")
def deleteItem(id:int, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item deleted'