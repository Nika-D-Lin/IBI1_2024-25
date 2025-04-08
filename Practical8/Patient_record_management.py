class patients(): #set the class
    def __init__(self, patient_name, age, date_of_latest_admission, medical_history): #set the self function
        self.patient_name = patient_name
        self.age = age
        self.data_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def print_details(self): #set the conteined function to print the target information
        print(f"Name: {self.patient_name}, Age: {self.age}, Admission Date: {self.data_of_latest_admission}, Medical History: {self.medical_history}")

#example:
patient1 = patients(patient_name = "Nika", age = 19, date_of_latest_admission = "2025.4.7", medical_history="Depressive disorder")
patient1.print_details()
#it will print: 'Name: Nika, Age: 19, Admission Date: 2025.4.7, Medical History: Depressive disorder'