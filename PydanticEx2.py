from pydantic import BaseModel
class UserData(BaseModel):
    name:str
    age:int
    percentage:float
    IsPresent:bool
data={"name":"aasif","age":23,"percentage":34.2,"IsPresent":True}
userobj=UserData(**data)
print(userobj)