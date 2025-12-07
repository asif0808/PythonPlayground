from typing import List,Dict
from pydantic import BaseModel
class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str,int]

data={"user_id":1,"items":["pen","note","keys"],"quantities":{"pen":2,"note":4,"keys":6}}
obj=Cart(**data)
print(obj)