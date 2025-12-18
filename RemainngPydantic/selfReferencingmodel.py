from pydantic import BaseModel
from typing import Optional,List
class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List["Comment"]]=None
Comment.model_rebuild()
c=Comment(id=1,content="first comment",replies=[Comment(id=2,content="first reply")])
print(c)