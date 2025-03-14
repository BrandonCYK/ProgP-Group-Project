#CSV library imported to help with file handling methods
import csv

#datetime module to help with date objects
import datetime

#initalize main lists
students = []
courses = []
enrolments = []

#initialize list fieldnames (to identify data columns)
student_fields = ['studentid', 'name', 'contact']
course_fields = ['courseid', 'name', 'seats']
enrolment_fields = ['studentid', 'courseid', 'dateofenrolment']

#Function to display the main user interface
def showMain():
    # Providing options for user to choose
    print("Welcome to the Course Management System!")
    while True:
        print("\n|Actions|")
        print("[1] Add a new student")
        print("[2] Add a new course")
        print("[3] Enrol in a course")
        print("[4] Drop a course")
        print("[5] View available courses")
        print("[6] View student information")
        print("[Q] Exit")

        # Taking in user input
        action = input("Please select your choice:").capitalize() # To capitalize the Q if a lowercase is entered
        if action == "1": # User wants to register a new student
            addStudent() #Run the function to register a new student

        elif action == "2": # User wants to add a new course
            addCourse() #Run the function to add a new course

        elif action == "3": # User wants to enroll a student into an existing course
            enrollCourse() #Run the function to enroll student into a course

        elif action == "4": # User wants to de-register a student from a course that the student enrolled
            dropCourse() #Run the function to de-register a student from course enrolment

        elif action == "5": # User wants to view all courses and their information
            viewCourses() #Run the function to view all course info

        elif action == "6": # User wants to view all registered student details
            viewStudents() #Run the function to view all registered student info

        elif action == "Q": # User wants to quit the system
            print("Thank you! Have a nice day!")
            saveData() # Run the function to store new data
            break

        else: #User input did not match any case, error is displayed. The main interface is displayed again
            print("You've entered an invalid character. Please try again.")

#Function to register a new student
def addStudent():
    #Initalize a list to store the new student's details
    newStudent = []
    print("You are registering a new student to the system. If you wish to return to the main interface, press the Enter key on any input prompt")
    
    # Taking in student details
    while True:
        student_ID = input("Fill in student ID:")

        if student_ID == "": #cancel action
            print("Returning")
            return
        
        #Validation
        if not checkStudentReg(student_ID): #check whether student ID already exists (ensure no duplicates)
            #if student ID not found, add student ID to list and break the loop
            newStudent.append(student_ID)
            break
        else: #if student ID found, print error message
            print("The student ID that you entered is already registered! Please register with another ID.")

    while True:
        student_name = input("Fill in student's name:")

        if student_name == "": #cancel action
            print("Returning")
            return

        #Validation
        if not student_name.isalpha(): #check whether student name contains any characters outside the alphabet
            #if yes, print error message
            print("Error: Name cannot contain any numbers or symbols! Name should only contain letters from the alphabets.")
        else:
            #if no, add name to list and break the loop
            newStudent.append(student_name)
            break
            
    while True:
        student_contact = input("Fill in student's contact:")
        
        if student_contact == "": #cancel action
            print("Returning")
            return

        if not student_contact.isdigit(): #check whether contact number contains any characters except the numbers
            #if yes, print error message
            print("Error: Contact number cannot contain any letters or symbols! Only numbers are allowed")
        else:
            #if no, add contact number to list and break the loop
            newStudent.append(student_contact)
            break
    
    # Display student details
    print(f'Student ID: {student_ID}\nStudent Name: {student_name}\nStudent Contact: {student_contact}')

    #Confirmation
    response = input("Confirm student registration? (Y - yes/Any key - cancel)").capitalize()

    if response == 'Y': #if confirmed
        #The expression below is called dictionary comprehension
        #The student fieldnames and the new student details are combined into a dictionary as key:value pairs
        toDict = {key:value for (key,value) in zip(student_fields, newStudent)}

        #Then, the new student is added to the student list
        students.append(toDict)
        print("Student registration successful!") #print message
    else: #if cancelled
        print("Student registration cancelled! Returning to main interface") #print message
        return
    

#Function to add a new course
def addCourse():
    #Initalize a list to store the new course details
    newCourse = []
    print("You are adding a new course. If you wish to return to the main interface, press the Enter key on any input prompt. (Works only for string inputs)")
    
    # Taking in course details
    while True:
        course_ID = input("Fill in the course ID:")

        if course_ID == "": #cancel action
            print("Returning")
            return
        
        #Validation
        if not checkCourseReg(course_ID): #check whether course ID already exists (ensure no duplicates)
            #if course ID not found, add course ID to list and break the loop
            newCourse.append(course_ID)
            break
        else: #if course ID found, print error message
            print("Error: The course ID that you entered is already registered! Please fill in another ID.")
            
    course_name = input("Fill in the name of the course:")
    if course_name == "": #cancel action
        print("Returning")
        return
    
    #add course name to list
    newCourse.append(course_name)
    
    while True: # Keep looping until an integer is entered
        try:
            course_seats = int(input("Fill in the maximum seats required for this course:"))

            #add course capacity to list
            newCourse.append(course_seats)
            break # Exit the loop once the input is an integer.
        except ValueError:
            print("Error: Invalid input. Please enter an integer.") # Error message for non-integer values

    # Display course details
    print(f'Course ID: {course_ID}\nCourse Name: {course_name}\nMaximum seats: {course_seats}')

    #Confirmation
    response = input("Confirm course registration? (Y - yes/Any key - cancel)").capitalize()

    if response == 'Y': #if confirmed
        #The expression below is called dictionary comprehension
        #The course fieldnames and the new course details are combined into a dictionary as key:value pairs
        toDict = {key:value for (key,value) in zip(course_fields, newCourse)}

        #Then, added new course to the course list
        courses.append(toDict)
        print("Course registration successful!") #print message
    else: #if cancelled
        print("Course registration cancelled! Returning to main interface") #print message
        return


#Function to enroll student into a course
def enrollCourse():
    #Initalize a list to store the enrolment details
    newEnrolment = []
    print("You are enroling a student into a course. If you wish to return to the main interface, press the Enter key on any input prompt.")
    student_enroll = ""
    while True:
        #Selecting student to enroll
        student_enroll = input("Fill in student ID:")

        if student_enroll == "": #cancel action
            print("Returning")
            return

        # Validation
        if checkStudentReg(student_enroll): #check whether student ID is registered
            #if registered, add the student's ID to the list and break the loop
            newEnrolment.append(student_enroll)
            break
        else: #if not registered, an option to register a new student is given or else the loop restarts
            print("Error: The student ID you entered is not valid!")
            #offer user option to register the new student first then enroll in the course
            response = input("Do you want to register a new student ID instead?\n[Y] Yes\n[Any key] Try another student ID").capitalize()

            #if user chooses to register a new student ID,
            if response == 'Y':
                addStudent() #Run the function to register a new student
                enrollCourse() #then Run the function to enroll student into a course
                return #Returns the user to the main interface, no need to continue on
            
    # Identifying the course that the student is enrolling in
    while True:
        course_enroll = input("Fill in the course ID:")

        if course_enroll == "": #cancel action
            print("Returning")
            return
        
        # Validation
        if checkCourseReg(course_enroll): #check whether course ID is registered
            if not checkStudentEnrolled(student_enroll, course_enroll): #check whether student ID is already enrolled into the course
                if getNumberOfSeats(course_enroll) <= 0: #check whether course still has capacity for an enrolment
                    #if no seats left, print error message
                    print("Error: The course has no more available seats left! Please try again later or choose another course.")
                else: #if there are seats available, add the course ID to the list and break the loop
                    newEnrolment.append(course_enroll)
                    break
            else:
                #if already enrolled into the course, print error message
                print("Error: The student ID you entered is already enrolled in the course! Please choose another course.")
        else: #if not registered, print error message
            print("Error: The course ID you entered is not valid! Please try again.")

    #Confirmation
    response = input(f"Confirm enrolment into Course {course_enroll}? (Y - yes/Any key - cancel)").capitalize()

    if response == 'Y': #if confirmed
        #Update number of seats
        updateCourseSeats(course_enroll, -1) #the -1 is the increment/decrement value

        #Record date of enrolment
        currentDate = str(datetime.date.today()) #get current date through datetime object
        newEnrolment.append(currentDate) #add the current date to the list
        
        #The expression below is called dictionary comprehension
        #The course fieldnames and the new course details are combined into a dictionary as key:value pairs
        toDict = {key:value for (key,value) in zip(enrolment_fields, newEnrolment)}

        #Then, added new course to the course list
        enrolments.append(toDict)
        print(f'Student successfully enrolled in Course {course_enroll}') #print message
    else: #if cancelled
        print("Course enrolment cancelled! Returning to main interface") #print message
        return


#Function to update the course capacity
def updateCourseSeats(course_ID, increment):
    for course in courses:
        if course['courseid'] == course_ID:
            course['seats']+=increment


#Function to get the course capacity
def getNumberOfSeats(course_ID):
    for course in courses: #finding the course
        if course['courseid'] == course_ID: #if course is found in the list
            return course['seats'] #return the course capacity

    #if course is not found
    return 0


#Function to drop a student from enrolling a course
def dropCourse():
    print("You are dropping a student from being enrolled in the course. If you wish to return to the main interface, press the Enter key on any input prompt.")
    
    # Identifying the student
    while True:
        #Selecting student to drop
        student_drop = input("Fill in student ID:")

        if student_drop == "": #cancel action
            print("Returning")
            return
        
        # Validation
        if checkStudentReg(student_drop): #check whether student ID is registered
            #if registered, break the loop
            break
        else: #if not registered, print error message
            print("Error: The student ID you entered is not valid!")
            
    # Identifying the course that the student wants to enrol in
    while True:
        course_drop = input("Fill in the course ID:")

        if course_drop == "": #cancel action
            print("Returning")
            return

        # Validation
        if checkCourseReg(course_drop): #check whether course ID is registered
            if not checkStudentEnrolled(student_drop, course_drop): #check whether student ID is enrolled into the course
                #if not enrolled into the course, print error message
                print("Error: The student ID you entered is not enrolled in the course! Please choose another course.")
            else: #if enrolled into the course, break loop
                break
        else: #if not registered, print error message
            print("Error: The course ID you entered is not valid! Please try again.")
            
    #Find enrolment index in the main enrolment list
    index = 0 #to locate the desired enrolment record
    for enrolment in enrolments:
        if student_drop == enrolment['studentid'] and course_drop == enrolment['courseid']: #if the enrolment has the same student ID and course ID
            updateCourseSeats(course_drop, 1) #when course is dropped, a seat is freed up
            #break the loop
            break
        else: #if not
            #increment the index
            index+=1

    #Delete course enrolment record from the list
    droppedRow = enrolments.pop(index) #store deleted enrolment record
    print(f"Student successfully dropped Course {droppedRow['courseid']}") #print message

    
#Function to view all courses
def viewCourses():
    return 0

        
#Function to view all student info
def viewStudents():
    return 0

        
#Function to verify student is registered
def checkStudentReg(student_ID):
    #check whether student ID exists in student list
    for student in students:
        if student_ID == student['studentid']: #if student ID exists
            return True
    
    #if student ID does not exist
    return False

#Function to verify course is registered
def checkCourseReg(course_ID):
    #check whether course ID exists in course list
    for course in courses:
        if course_ID == course['courseid']: #if course ID exists
            return True
        
    #if course ID does not exist
    return False

#Function to verify student is enrolled into a course
def checkStudentEnrolled(student_ID, course_ID):
    #check whether student ID is enrolled in the course in enrollment list
    for enrolment in enrolments:
        if student_ID == enrolment['studentid'] and course_ID == enrolment['courseid']: #if student is enrolled into the course
            return True
        
    #if student is not enrolled into the course
    return False

#Function to retrieve student info from file and store into a list
def retrieveStudents():
    row_count = 0 #number of rows read
    try: #read students.csv
        with open('students.csv') as student_file: #open file in read mode (default)
            csv_reader = csv.DictReader(student_file) #initalize CSV reader object, pass in student file to be read
            for row in csv_reader:
                #object returns a collection, store each row into the main student list
                students.append(row)
                row_count+=1 #update counter

    except FileNotFoundError: #if students.csv does not exist
        print("Warning: students.csv not found! New file created.") #print error message

        with open('students.csv', 'w') as student_file: #open file in write mode (to create a new file)
            csv_writer = csv.DictWriter(student_file, fieldnames=student_fields) #initalize CSV writer object, pass in student file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers
            
    else: #if no errors occur
        print(f"{row_count} student rows processed and retrieved.") #print message to display completion of data retrieval
        
        
#Function to retrieve course info from file and store into a list
def retrieveCourses():
    row_count = 0 #number of rows read
    try: #read courses.csv
        with open('courses.csv') as course_file: #open file in read mode
            csv_reader = csv.DictReader(course_file) #initialize CSV reader object, pass in course file to be read
            for row in csv_reader:
                row['seats'] = int(row['seats']) #convert the field 'seats' into integer
                
                #object returns a collection, store each row into the main course list
                courses.append(row)
                row_count+=1 #update counter
                
    except FileNotFoundError: #if courses.csv does not exist
        print("Warning: courses.csv not found! New file created.") #print error message

        with open('courses.csv', 'w') as course_file: #open file in write mode
            csv_writer = csv.DictWriter(course_file, fieldnames=course_fields) #initialize CSV writer object, pass in course file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers
            
    else: #if no errors occur
        print(f"{row_count} course rows processed and retrieved.") #print message to display completion of data retrieval
        


#Function to retrieve course enrolment info from file and store into a list
def retrieveEnrols():
    row_count = 0 #number of rows read
    try: #read enrolments.csv
        with open('enrolments.csv') as enrolment_file: #open file in read mode
            csv_reader = csv.DictReader(enrolment_file) #initialize CSV reader object, pass in enrolment file to read
            for row in csv_reader:
                #object reutnrs a collection, store each row into the main course list
                enrolments.append(row)
                row_count+=1 #update counter
                
    except FileNotFoundError: #if enrolments.csv does not exist
        print("Warning: enrolments.csv not found! New file created.") #print error message

        with open('enrolments.csv', 'w') as enrolment_file: #open file in write mode
            fieldnames = ['studentid', 'courseid', 'dateofenrolment'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(enrolment_file, fieldnames=fieldnames) #initialize CSV writer object, pass in enrolment file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers

    else: #if no errors occur
        print(f"{row_count} enrolment rows processed and retrieved.") #print message to display completion of data retrieval

        
#Function to overwrite new data into respective files
def saveData():
    #PART 1: Saving student records
    try: #write students.csv
        with open('students.csv', 'w') as student_file: #open file in write mode 
            csv_writer = csv.DictWriter(student_file, fieldnames=student_fields) #initalize CSV writer object, pass in student file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers
            for row in students:
                csv_writer.writerow(row) #store each row into students.csv

    except: #if an error occurs
        print("Unexpected Error: Data saved unsuccessfully! Please try again.") #print error message, abort

    else: #if no errors occur
        print(f"{len(students)} student records saved successfully!") #print message to display completion of data persistence

    #PART 2: Saving course records
    try: #write courses.csv
        with open('courses.csv', 'w') as course_file: #open file in write mode
            csv_writer = csv.DictWriter(course_file, fieldnames=course_fields) #initalize CSV writer object, pass in course file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers
            for row in courses:
                csv_writer.writerow(row) #store each row into courses.csv

    except: #if an error occurs
        print("Unexpected Error: Data saved unsuccessfully! Please try again.") #print error message, abort

    else: #if no errors occur
        print(f"{len(courses)} course records saved successfully!") #print message to display completion of data persistence

    #PART 3: Saving course enrolment records
    try: #write enrolments.csv
        with open('enrolments.csv', 'w') as enrolment_file: #open file in write mode 
            csv_writer = csv.DictWriter(enrolment_file, fieldnames=enrolment_fields) #initalize CSV writer object, pass in enrolment file and fieldnames

            csv_writer.writeheader() #write fieldnames into file as headers
            for row in enrolments:
                csv_writer.writerow(row) #store each row into enrolments.csv

    except: #if an error occurs
        print("Unexpected Error: Data saved unsuccessfully! Please try again.") #print error message, abort

    else: #if no errors occur
        print(f"{len(enrolments)} enrolment records saved successfully!") #print message to display completion of data persistence
        

#MAIN PROGRAM STARTS HERE >
retrieveStudents() #retrieve students
retrieveCourses() #retrieve courses
retrieveEnrols() #retrieve course enrolments
showMain() #display main interface

