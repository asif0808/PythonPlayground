from pydantic import BaseModel,model_validator
class SignupData(BaseModel):
    password:str
    confirm_password:str
    @model_validator(mode="after")
    def password_match(cls,vals):
        if vals.password!=vals.confirm_password:
            raise ValueError("pasword not matched")
        return vals
obj=SignupData(password="1234",confirm_password="1234")
print(obj)