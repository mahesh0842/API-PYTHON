from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(min_length=3, max_length=50,description="Name of the patient",examples=["John Doe","Jane Smith"])]  # name should be between 3 and 50 characters
    email:EmailStr
    age:int
    weight:float
    married:Optional[bool]=None 
    #if patient dont want to provide their married dastils we can put them optional and dont need in our rawa data 
    allergies:List[str]
    contact_details:Dict[str,str]
    linkedin_url:AnyUrl

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.linkedin_url)
    
    print('inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info={'name':'mahesh','email':'abc@gmail.com','age':30,'weight':75.2,'married':True ,'allergies':['pollen','dust'],'contact_details':{'emails':"abc@gmail.com",'phone':'123456789'},'linkedin_url':'http://linkedin.com/1323'}#dictonary raw data


patient1=Patient(**patient_info)#object of patient class 
insert_patient_data(patient1)
update_patient_data(patient1)
