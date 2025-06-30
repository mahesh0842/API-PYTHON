from fastapi import FastAPI,Path,HTTPException,Query
#path is a function provide metadata validation for path parameters 
import json
app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data= json.load(f)
    return data
       



@app.get("/")
def hello():
    return {"message": "Patient Management System API"}
@app.get("/about")
def about():
    return {"message": " fully Patient Management System API for managing patient records, appointments, and medical history."} 

@app.get("/View")
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='description in db',example='P001')):
    #load all patient data
    data = load_data()
    #find the patient with the given id

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="patient not found")
#sorting the data using key value pair using query parameter
@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description="sort basis on height weight and bmi"),order:str =Query('asc',description='sort asc or desc order')):
    valid_fields=['height','weight','Bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='invalid order between asc or desc')
    data=load_data()

    sort_order =True if order=='desc'else False
    sorted_data = sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=False)
    return sorted_data