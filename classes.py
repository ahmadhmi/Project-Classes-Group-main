#All classes contain a format function that re-formats object data into the text data it was read from
class Doctor:
    doctorList = []
    def __init__(self, id, name, specialty, schedule, qualification, room):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.qualification = qualification
        self.room = room
        Doctor.doctorList.append(self)

    def __str__(self):
        result = f"{self.id:<4s}{self.name:<15s}{self.specialty:<18s}{self.schedule:<25s}{self.qualification:<20s}{self.room:<7s}"
        return result

    def formatDoctorInfo(self):
        result = f"{self.id}_{self.name}_{self.specialty}_{self.schedule}_{self.qualification}_{self.room}\n"
        return result

    def sortDoctorById():
        Doctor.doctorList.sort(key=getId)

class Facility:
    facilityList = []
    def __init__(self, name):
        self.name = name
        Facility.facilityList.append(self)

    def __str__(self):
        result = f"{self.name}"
        return result

    def formatFacilityInfo(self):
        result = f"{self.name}\n"
        return result

    def sortFacilityByName():
        Facility.facilityList.sort(key=getName)

class Laboratory:
    laboratoryList = []
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        Laboratory.laboratoryList.append(self)

    def __str__(self):
        result = f"{self.name:<25s}{self.cost:<25s}"
        return result

    def formatLaboratoryInfo(self):
        result = f"{self.name}_{self.cost}\n"
        return result

    def sortLaboratoryByName():
        Laboratory.laboratoryList.sort(key=getName)

class Patient:
    patientList = []
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
        Patient.patientList.append(self)

    def __str__(self):
        result = f"{self.id:<10s}{self.name:<15s}{self.diagnosis:<15s}{self.gender:<15s}{self.age:<15s}"
        return result
    
    def formatPatientInfo(self):
        result = f"{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}\n"
        return result

    def sortPatientById():
        Patient.patientList.sort(key=getId)        

def getId(object):
    if not object.id.isdigit():
        return 0
    else:
        return int(object.id)

def getName(object):
    if object.name in ["Facilities:", "Lab Name"]:
        return "A"
    else:
        return object.name