from classes import Doctor, Laboratory, Facility, Patient

# Defining information buffers (Dictionaries)
DOCTORINFO = {  "id": "", "name": "", "specialty": "","schedule": "", "qualifications": "", "room number": ""}
FACILITYINFO = {"name": ""}
LABORATORYINFO = {  "name": "", "cost": ""}
PATIENTINFO = {     "id": "", "name": "",    "diagnosis": "", "gender": "", "age": ""}
DOCTORINFO = {"id": "", "name": "", "specialty": "", "schedule": "", "qualifications": "", "room number": ""}
FACILITYINFO = {"name": ""}
LABORATORYINFO = {"name": "", "cost": ""}
PATIENTINFO = {"id": "", "name": "", "diagnosis": "", "gender": "", "age": ""}

#Defining menu messages
MAIN_MENU_MESSAGE = """
Welcome to the Alberta Rural Patient Care Management System

Main Menu
0 - Close application
1 - Doctors
2 - Facilities
3 - Laboratories
4 - Patients
Enter Option: """

DOCTOR_MENU_MESSAGE = """
Doctor's Menu
0 - Return to Main Menu
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by Name
4 - Add doctor
5 - Edit doctor Info
Enter Option: """

FACILITY_MENU_MESSAGE = """
Facilities Menu
0 - Return to Main Menu
1 - Display Facilities List
2 - Add Facility
Enter Option: """

LABORATORY_MENU_MESSAGE = """
Laboratory Menu
0 - Return to Main Menu
1 - Display laboratories list
2 - Add laboratory
Enter Option: """

PATIENT_MENU_MESSAGE = """
Patient Menu
0 - Return to Main Menu
1 - Display Patient's list
2 - Search for patients by ID
3 - Add patient
4 - Edit patient Info
Enter Option: """

#Validates input; displays an error and re-prompts for input if values do not match the conditions
def validateRangeInput(inputNumber, inputRangeLow, inputRangeHigh):
    while not inputNumber.isdigit() or not int(inputNumber) in range(inputRangeLow, inputRangeHigh):
        inputNumber = input("Please enter a valid option: ")
    return int(inputNumber)

#Defining the function to validate integer inputs
def validateIntegerInput(inputNumber):
    while not inputNumber.isdigit():
        inputNumber = input("Please enter an integer: ")
    return str(inputNumber)

#Defining the function to determine if an id is currently being used
def validateIdInput(id, objectList):
    while not searchById(objectList, id) == -1:
        id = input("The entered ID is currently in use. Please enter a different ID: ")
    return str(id)

#Menu functions. Menus are navigated through letter keys 1-9, with 0 exiting
def mainMenu():
    option = validateRangeInput(input(MAIN_MENU_MESSAGE), 0, 5)
    print("")
    while option > 0:
        if option == 1:
            doctorsMenu()
        elif option == 2:
            facilitiesMenu()
        elif option == 3:
            laboratoriesMenu()
        elif option == 4:
            patientsMenu()
        option = validateRangeInput(input(MAIN_MENU_MESSAGE), 0, 5)

def doctorsMenu():
    doctorOption = validateRangeInput(input(DOCTOR_MENU_MESSAGE), 0, 6)
    print("")
    while doctorOption > 0:
        if doctorOption == 1:
            displayInfo(Doctor.doctorList)
        elif doctorOption == 2:
            id = input("\n\nEnter the doctor ID: ")
            doctor = searchById(Doctor.doctorList, id)
            displayIndividualDoctor(doctor, id)
        elif doctorOption == 3:
            name = input("\n\nEnter the doctor Name: ")
            doctor = searchByName(Doctor.doctorList, name)
            displayIndividualDoctor(doctor, name)
        elif doctorOption == 4:
            enterDoctorInfo()
        elif doctorOption == 5:
            id = input("Enter the Doctor's ID: ")
            editDoctorInfo(id)
        doctorOption = validateRangeInput(input(DOCTOR_MENU_MESSAGE), 0, 6)
    else:
        Doctor.sortDoctorById()
        writeListToFile("data/doctors.txt", Doctor.doctorList, Doctor.formatDoctorInfo)

def facilitiesMenu():
    facilityOption = validateRangeInput(input(FACILITY_MENU_MESSAGE), 0, 3)
    while facilityOption > 0:
        print("")
        if facilityOption == 1:
            displayInfo(Facility.facilityList)
        elif facilityOption == 2:
            enterFacilityInfo()
        facilityOption = validateRangeInput(input(FACILITY_MENU_MESSAGE), 0, 3)
    else:
        Facility.sortFacilityByName()
        writeListToFile("data/facilities.txt", Facility.facilityList, Facility.formatFacilityInfo)

def laboratoriesMenu():
    laboratoryOption = validateRangeInput(input(LABORATORY_MENU_MESSAGE), 0, 3)
    while laboratoryOption > 0:
        print("")
        if laboratoryOption == 1:
            displayInfo(Laboratory.laboratoryList)
        elif laboratoryOption == 2:
            enterLaboratoryInfo()
        laboratoryOption = validateRangeInput(
            input(LABORATORY_MENU_MESSAGE), 0, 3)
    else:
        Laboratory.sortLaboratoryByName()
        writeListToFile("data/laboratories.txt", Laboratory.laboratoryList, Laboratory.formatLaboratoryInfo)

def patientsMenu():
    patientOption = validateRangeInput(input(PATIENT_MENU_MESSAGE), 0, 5)
    while patientOption > 0:
        print("")
        if patientOption == 1:
            displayInfo(Patient.patientList)
        elif patientOption == 2:
            id = input("Enter the Patient ID: ")
            patient = searchById(Patient.patientList, id)
            displayIndividualPatient(patient, id)
        elif patientOption == 3:
            enterPatientInfo()
        elif patientOption == 4:
            id = input("Enter the Patient's ID: ")
            editPatientInfo(id)
        patientOption = validateRangeInput(input(PATIENT_MENU_MESSAGE), 0, 5)
    else:
        Patient.sortPatientById()
        writeListToFile("data/patients.txt", Patient.patientList, Patient.formatPatientInfo)

#Reads a file and imports its contents to an object.
#The second argument determines which type of class to store the file as.
def readFile(path, objectClass):
    with open(path, "r") as file:
        for line in file:
            entry = line.rstrip().split("_")
            if line:
                objectClass(*entry)

#Searches a list of object structures to find an object with a matching ID
def searchById(objectList, id):
    for entry in objectList:
        if entry.id == id:
            return entry
    else:
        return -1

#Searches a list of object structures to find an object with a matching name
def searchByName(objectList, name):
    for entry in objectList:
        if entry.name == name:
            return entry
    else:
        return -1

#Displays all of the info of the objects in a list using the object's str method
def displayInfo(objectList):
    for object in objectList:
        print(object)

def addToList(objectList):
    entry = enterDoctorInfo(objectList)
    objectList.append(entry)
    return objectList

#Writes a list of objects' data to a file
def writeListToFile(path, objectList, classMethod):
    with open(path, "w") as file:
        for entry in objectList:
            data = classMethod(entry)
            file.write(data)

#Allows for adding and modifying doctor data
def enterDoctorInfo():
    newInfo = getInfo(DOCTORINFO)
    Doctor(newInfo["id"], newInfo["name"], newInfo["specialty"], newInfo["schedule"], newInfo["qualifications"], newInfo["room number"])

def editDoctorInfo(id):
    doctor = searchById(Doctor.doctorList, id)
    displayIndividualDoctor(doctor, id)
    newInfo = getInfo(DOCTORINFO, True)
    if not doctor == -1:
        doctor.name = newInfo["name"]
        doctor.specialty = newInfo["specialty"]
        doctor.schedule = newInfo["schedule"]
        doctor.qualification = newInfo["qualifications"]
        doctor.room = newInfo["room number"]
        displayInfo(Doctor.doctorList)

#Displays the data of a given doctor. Displays an error if the doctor does not exist.
def displayIndividualDoctor(doctor, id):
    if doctor == -1 and id.isdigit():
        print(f"Doctor with ID {id} not found in file")
    elif doctor == -1 and not id.isdigit():
        print(f"Doctor {id} not found in file")
    else:
        print(doctor)

#Adds new facilities and laboratories.
def enterFacilityInfo():
    newInfo = getInfo(FACILITYINFO)
    Facility(newInfo["name"])

def enterLaboratoryInfo():
    newInfo = getInfo(LABORATORYINFO)
    Laboratory(newInfo["name"], newInfo["cost"])

#Allows for adding and modifying patient data
def enterPatientInfo(): 
    newInfo = getInfo(PATIENTINFO)
    Patient(newInfo["id"], newInfo["name"], newInfo["diagnosis"], newInfo["gender"], newInfo["age"])

def editPatientInfo(id):
    patient = searchById(Patient.patientList, id)
    displayIndividualPatient(patient, id)
    newInfo = getInfo(PATIENTINFO, True)
    if not patient == -1:
        patient.name = newInfo["name"]
        patient.diagnosis = newInfo["diagnosis"]
        patient.gender = newInfo["gender"]
        patient.age = newInfo["age"]
        displayInfo(Patient.patientList)

#Displays the data of a given patient. Displays an error if the patient does not exist.
def displayIndividualPatient(patient, id):
    if patient == -1:
        print(f"Patient with ID {id} not in patient file")
    else:
        print(patient)

# A generalized getInfo function is declared, a type of information buffer (an empty dict of desired info) and a mode bool is passed in
def getInfo(bufferType, mode=False):
    # initializing a copy of the buffer type
    infoBuffer = dict(bufferType)

    # defining a string to store a message corresponding to the class type
    classType = "Enter"

    # storing the class that will be used to validate an id
    idValidator = ""

    # initializing those variables based on the argument passed in
    if not mode:
        if str(bufferType) == str(DOCTORINFO):
            classType += " Dr"
            idValidator = Doctor.doctorList
        elif str(bufferType) == str(FACILITYINFO):
            classType += " Facility"
        elif str(bufferType) == str(LABORATORYINFO):
            classType += " Lab"
        elif str(bufferType) == str(PATIENTINFO):
            classType += " Patient"
            idValidator = Patient.patientList

    # editing the message based on the mode
    if mode:
        classType += " new"

    # for every key inside the information buffer...
    for key in infoBuffer:
        # (if mode is true and the key == id, skip to the next key)
        if mode and key == "id":
            continue
        # (complete the message to be printed)
        message = f"{classType} {key.capitalize()}: "
        # match the key and update its value
        match key:
            case "id":
                infoBuffer[key] = validateIdInput(
                    validateIntegerInput(input(message)), idValidator)
            case "name":
                infoBuffer[key] = input(message).title()
            case "specialty":
                infoBuffer[key] = input(message).title()
            case "schedule":
                infoBuffer[key] = input(message).lower()
            case "qualifications":
                infoBuffer[key] = input(message).upper()
            case "room number":
                infoBuffer[key] = validateIntegerInput(input(message))
            case "result":
                infoBuffer[key] = input(message).title()
            case "cost":
                infoBuffer[key] = validateIntegerInput(input(message))
            case "diagnosis":
                infoBuffer[key] = input(message).title()
            case "gender":
                infoBuffer[key] = input(message).title()
            case "age":
                infoBuffer[key] = validateIntegerInput(input(message))
    #When all the desired information has been entered, return the buffer for use in another function
    return infoBuffer