from pydantic import BaseModel,field_validator
class User(BaseModel):
    name:str
    @field_validator('name')
    def name_length(cls,n):
        if len(n)<4:
            raise ValueError("name is short")
        return n
user=User(name="john")
print(user)