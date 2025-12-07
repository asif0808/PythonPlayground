# Pydantic : mainly used for data type validation
from pydantic import BaseModel
class UserData(BaseModel):
    name:str
    age:int
    marks:int
    gender:str
user=UserData(name="aasif",age=23,marks=65,gender="male")
print(user)
# print(user.dict)