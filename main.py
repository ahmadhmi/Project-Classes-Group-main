#Hospital Management program for Alberta Rural Patient Care
#By Angelo Fernando, John Dao, Charles Ashmore, and Ahmad Heshmati
#December 11, 2022
#Allows the user to view, search, and modify data regarding doctors, facilities, laboratories, and patients.
#The user may choose which data type to view from a manin menu, which opens up a relevant submenu
#Patient data shows the patients' names, diagnoses, genders, and ages
#Patients may be freely added and modified, as well as searched by ID
#Doctor data shows the doctors' names, specialties, schedules, qualificaitons, and assigned rooms
#Doctors may be freely added and modified, as well as searched by ID or name.
#Facilities and laboritories can be viewed, and extra facilities or laboritories may be added.

import management
import classes

def main():
    management.readFile("data/doctors.txt", classes.Doctor)
    management.readFile("data/facilities.txt", classes.Facility)
    management.readFile("data/laboratories.txt", classes.Laboratory)
    management.readFile("data/patients.txt", classes.Patient)
    management.mainMenu()

if __name__ == "__main__":
    main()