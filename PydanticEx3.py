from pydantic import BaseModel
class Cart(BaseModel):
    user_id:int
    items:list[str]
    quantities:dict[str,int]

data={"user_id":1,"items":["pen","note","keys"],"quantities":{"pen":2,"note":4,"keys":6}}
obj=Cart(**data)
print(obj)