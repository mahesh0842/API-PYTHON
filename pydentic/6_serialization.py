from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)
#covert it on python dictonary
# temp = patient1.model_dump() # default is exclude_none=False, exclude_unset=False
# temp = patient1.model_dump(exclude_none=True) # exclude_none=True, exclude_un
temp = patient1.model_dump(exclude_unset=True)
temp1=patient1.model_dump(exclude=['name','gender'])

print(temp)
print('TEMP 2 = ',temp1)
print(type(temp))
