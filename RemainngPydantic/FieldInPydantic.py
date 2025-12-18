from pydantic import BaseModel,Field
class Student(BaseModel):
    name:str=Field(...,min_length=4,max_length=10)
    marks:int
    sid:int
    salary:float=Field(...,ge=10000,le=20000)
student=Student(name="john",marks=43,sid=32,salary=12242)
print(student)