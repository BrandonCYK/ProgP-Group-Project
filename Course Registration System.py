#CSV library imported to help with file handling methods
import csv

#initalize main lists
students = []
courses = []
enrolments = []

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
    print("You are registering a new student to the system.")
    # Taking in student details
    while True:
        student_ID = input("Fill in student ID:")

        #Validation
        if not checkStudentReg(student_ID): #check whether student ID already exists (ensure no duplicates)
            #if student ID not found,
            break
        else: #if student ID found, print error message
            print("The student ID that you entered is already registered in the system database! Please register with another ID.")
            
    student_name = input("Fill in student's name:")
    student_contact = input("Fill in student's contact:")
    # Display student details before storing in the text file students.txt
    print(f'Student ID: {student_ID}\nStudent Name: {student_name}\nStudent Contact: {student_contact}')
    

#Function to add a new course
def addCourse():
    print("You are adding a new course.")
    # Taking in course details
    while True:
        course_ID = input("Fill in the course ID:")

        #Validation
        if not checkCourseReg(course_ID): #check whether course ID already exists (ensure no duplicates)
            #if course ID not found,
            break
        else: #if course ID found, print error message
            print("Error: The course ID that you entered is already registered in the system database! Please register with another ID.")
    course_name = input("Fill in the name of the course:")
    while True: # Keep looping until an integer is entered
        try:
            course_seats = int(input("Fill in the maximum seats required for this course:"))
            break # Exit the loop once the input is an integer.
        except ValueError:
            print("Error: Invalid input. Please enter an integer.") # Error message for non-integer values
    # Display course details before storing in the text file courses.txt
    print(f'Course ID: {course_ID}\nCourse Name: {course_name}\nMaximum seats: {course_seats}')

    
#Function to enroll student into a course
def enrollCourse():
    print("You are enroling a student into a course.")
    student_enroll = ""
    while True:
        #Selecting student to enroll
        student_enroll = input("Fill in student ID:")

        # Validation
        if checkStudentReg(student_enroll): #check whether student ID is registered
            #if registered, break the loop
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
        
        # Validation
        if checkCourseReg(course_enroll): #check whether course ID is registered
            if checkStudentEnrolled(student_enroll, course_enroll): #check whether student ID is already enrolled into the course
                #if already enrolled into the course, print error message
                print("Error: The student ID you entered is already enrolled in the course! Please choose another course.")
            else: #if not enrolled into the course yet, break loop
                break
        else: #if not registered, print error message
            print("Error: The student ID you entered is not valid! Please try again.")

    #Update number of seats
    course_seats -= 1
    print(f'You have successfully enrolled in {course_enrol}')

    
#Function to drop a student from enrolling a course
def dropCourse():
    print("You are dropping a student from being enrolled in the course.")
    student_drop = ""
    while True:
        #Selecting student to drop
        student_drop = input("Fill in student ID:")

        # Validation
        if checkStudentReg(student_drop): #check whether student ID is registered
            #if registered, break the loop
            break
        else: #if not registered, print error message
            print("Error: The student ID you entered is not valid!")
            
    # Identifying the course that the student wants to enrol in
    while True:
        course_drop = input("Fill in the course ID:")

        # Validation
        if checkCourseReg(course_enroll): #check whether course ID is registered
            if not checkStudentEnrolled(student_enroll, course_enroll): #check whether student ID is enrolled into the course
                #if not enrolled into the course, print error message
                print("Error: The student ID you entered is not enrolled in the course!")
            else: #if enrolled into the course yet, break loop
                break
        else: #if not registered, print error message
            print("Error: The student ID you entered is not valid! Please try again.")

    #Update number of seats
    course_seats += 1
    print(f'You have successfully dropped {course_drop}')

    
#Function to view all courses
def viewCourses():
    print("You are viewing all the available courses.")
    # Searching for the course in the text file courses.txt
    while course_ID == True:
    # Display all available courses and their details
        print(f'Course ID: {course_ID}\nCourse Name: {course_name}\nRemaining seats: {course_seats}')

        
#Function to view all student info
def viewStudents():
    print("You are viewing all of the students' information.")
    # Searching for the course in the text file courses.txt
    while student_ID == True:
    # Display all available courses and their details
        print(f'Student ID: {student_ID}\nCourse Name: {student_name}\nStudent Contact: {student_contact}')

        
#Function to verify student is registered
def checkStudentReg(student_ID):
    #check whether student id exists in student list
    #if student_id exists
    return True
    #if student_id does not exist
    #return False

#Function to verify course is registered
def checkCourseReg(course_ID):
    #check whether course ID exists in course list
    #if course ID exists
    return True
    #if course ID does not exist
    #return False

#Function to verify student is enrolled into a course
def checkStudentEnrolled(student_ID, course_ID):
    #check whether student ID exists in enrollment list
    #if student ID exists
    return True
    #if student ID does not exist
    #return False

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
            fieldnames = ['studentid', 'name', 'contact'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(student_file, fieldnames=fieldnames) #initalize CSV writer object, pass in student file and fieldnames

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
            fieldnames = ['courseid', 'name', 'seats'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(course_file, fieldnames=fieldnames) #initialize CSV writer object, pass in course file and fieldnames

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
            fieldnames = ['studentid', 'name', 'contact'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(student_file, fieldnames=fieldnames) #initalize CSV writer object, pass in student file and fieldnames

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
            fieldnames = ['courseid', 'name', 'seats'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(course_file, fieldnames=fieldnames) #initalize CSV writer object, pass in course file and fieldnames

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
            fieldnames = ['studentid', 'courseid', 'dateofenrolment'] #fieldnames to identify columns
            csv_writer = csv.DictWriter(enrolment_file, fieldnames=fieldnames) #initalize CSV writer object, pass in enrolment file and fieldnames

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

