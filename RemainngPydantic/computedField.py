# computed_field used to derive field from other given fields
from pydantic import BaseModel,Field,computed_field
class Hotel(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,ge=1)
    rate_pr:int
    @computed_field
    @property
    def total_amount(self)->int:
        return self.nights*self.rate_pr
Hobj=Hotel(user_id=123,room_id=456,nights=2,rate_pr=2000)
print(Hobj.total_amount)