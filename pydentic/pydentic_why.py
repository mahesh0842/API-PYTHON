def insert_patient_data(name:str,age:int ):
    if type(name)==str and type(age)==int:
        if age<0:
            raise ValueError("age cant be negative")
        else:
            print(name)
            print(age)
            print("insert into databases")
    else:
        raise TypeError("incorrecrt data types")
    
    #update
def update_patient_data(name:str,age:int ):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("updated")
    else:
        raise TypeError("incorrecrt data types")
    
insert_patient_data("mk",30)