from pydantic import BaseModel

class Item(BaseModel):
    task:str
    # class Config:
    #     orm_mode = True
    