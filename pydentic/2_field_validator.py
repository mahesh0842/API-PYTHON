from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator,model_validator,computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float  #kgs
    height:float  #mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2) 
        return bmi


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise value('not valid domain')
        return value
    
    
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    

    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("age should be in between 0 to 100")
     
     
     #model validator   
    @model_validator(mode='after')
    def validate_emergency_contact_list(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("patint older than 60 must have an emergency contact ")  
        return model 


patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '30', 'weight': 75.2,'height':1.72, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462','emergency':'1234567889'}}

patient1 = Patient(**patient_info) # validation -> type coercion

def update_patient_data(patient:patient1):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('BMI',patient.bmi)
    print('updated')

update_patient_data(patient1)