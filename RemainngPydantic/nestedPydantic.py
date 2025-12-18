from pydantic import BaseModel
class Address(BaseModel):
    street:str
    city:str
    code:int
class User(BaseModel):
    name:str
    address:Address
address=Address(street="first",city="hyd",code=5432)
user=User(name="john",address=address)
print(user)
print(user.address)
# or
user_data={"name":"john","address":{
    "street":"123","city":"hyd","code":4543
}}
user=User(**user_data)
print(user)
print(user.address)