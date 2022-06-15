# =====importing libraries===========
from datetime import date   # this function gets the current date and time
'''gets the current day'''
today = date.today()
'''gets the current date in string form'''
daysDate = today.strftime("%d %B %Y")
#gets the directory in the file
import os.path
# ======functions section=======
def newfunc():
    file = open("user.txt", "r")
    nameList = []
    passwordList = []
    lines = file.readlines()
    for line in lines:
        temp = line.strip()
        temp = temp.split(", ")
        nameList.append(temp[0])
    print(nameList)
# register user function
def reg_user():
    '''open user file, welcome the user and allow for a new username and password'''
    file = open("user.txt", "a")
    print("Welcome new user!")

    '''username and password inputs'''
    newUsername = input("create username: ")
    #usercheck = newfunc()
    '''if the new username is in the namelist defined previously'''
    if newUsername in nameList:
        while newUsername in nameList:
            '''prompt user to enter another username'''
            newUsername = input("that username is take try again: ")
    else:
        print("good user name")
    '''prompts the user to input a password and confirm it'''
    newPassword = input("create password: ")
    conPassword = input("confirm password: ")

    '''if passwords do not match loop and prompt user to enter the correct password'''
    if newPassword != conPassword:
        while newPassword != conPassword:
            conPassword = input("passwords do not match enter again: ")

        '''once correct store username and password in newUser variable'''
        newUser = newUsername + ", " + newPassword

        '''welcome new user'''
        print("welcome {} \n".format(newUsername))

        '''add new user to user file'''
        file.write(str("\n" + newUser ))

    # if inputs are correct:
    else:
        """add user name and password together and store it in newUser"""
        newUser = newUsername + ", " + newPassword

        '''welcome the user'''
        print("welcome {}".format(newUsername))

        '''add user to user file'''
        file.write(str("\n" + newUser  ))
        file.close()

# add task function
'''this function opens the tasks.txt file and asks the user to input all the options of tasks and stores it in the tasks.txt'''
def add_task():
    '''open file and append'''
    file2 = open("tasks.txt", "a")
    taskUser = input("who would you like to assign a task to: ")
    taskName = input("enter the title of the task: ")
    taskDes = input("enter a description of the task: ")
    dueDate = input("enter the due date of the task eg. 20 may 2022: ")
    TheDate = today
    complete = "no"
    '''adds together all the options of the user and writes it to the file'''
    file2.write("\n" + taskUser + ", " + taskName + ", " + taskDes + ", " + dueDate + ", " + daysDate + ", " + complete)
    file2 = open("tasks.txt", "a")
    import sys
    output = ""  # looked up online how to do this
    with open("tasks.txt", "r+") as fy:
        for l in fy:
            if not l.isspace():
                '''writes new output to the empty string'''
                output += l
    fy = open("tasks.txt", "w")
    '''writes to the file the striped output'''
    fy.write(output)
    file2.close()

# view all function
'''the view all function allows the user to view all the tasks in the task.txt'''
def view_all():
    '''open the tasks file'''
    file2 = open("tasks.txt", "r")
    '''gets all the data in the file by reading the lines'''
    lines = file2.readlines()
    '''loops through the words in each line'''
    for line in lines:
        '''splits the words at the comma'''
        temp = line.split(", ")
        '''prints the data out in a easy to read way'''
        print(f'''
Task:               {temp[1]}
assigned to:        {temp[0]} 
date assigned:      {temp[3]}
due date:           {temp[4]}
task complete:      {temp[5]}
task description    {temp[2]}
                    ''')
    file2.close()

# view mine function
def view_mine():
    '''new list for the tasks to be stored in for easy editing and minipulation'''
    taskList = []
    '''count variable'''
    count = 0
    '''opens the task file'''
    file2 = open("tasks.txt", "r")
    '''reads all the lines once again'''
    lines = file2.readlines()

    '''for loop loops through the words in each line and appends each line to the list'''
    for line in lines:
        temp1 = line.split(", ")
        taskList.append(line)
        count += 1
        '''if the logged in username is equal to the username in the tasks then only display those tasks '''
        if userName == temp1[0]:
            print(f'''
Task:               {temp1[1]}
assigned to:        {temp1[0]} 
date assigned:      {temp1[3]}
due date:           {temp1[4]}
task complete:      {temp1[5]} 
task description    {temp1[2]}
''')

    #print(taskList)
    #print(count)
    #edit function in VM
    '''asks the user what task number to edit'''
    edit = input("select the task number to be edited: ")
    '''if statement triggered when user chooses the task no. '''
    if edit != "-1":
        '''index variable is equal to the input -1 as computers start at 0'''
        index = int(edit) - 1
        '''gets the line of the task using the list and the index'''
        line_list = taskList[index]
        print(f"{line_list}")
        '''splits the data using split function'''
        taskUser, taskName, taskDes, dueDate, daysDate, complete = line_list.split(", ")
        #line_list = line_list.split(", ")
        '''once the task is edited the if statement checks to see if it can be saved with a newline,
        meaning if it doesnt have a new line character it is edited otherwise it must be edited'''
        if complete == complete.strip("\n"):
            new_line = False
        else:
            new_line = True
        complete = complete.strip("\n")
        '''input for the user to select what must be edited'''
        edit_complete = input("c - mark task as complete \ne - edit task: ")
        '''edits complete from no to yes'''
        if edit_complete == "c":
            complete = "yes"
        #changes the user name to a specific input
        elif edit_complete == "e":
            new_user_name = input("Enter a new user name")
            taskUser = new_user_name
        #changes the date to a date specified
            new_date = input("Enter a new date")
            dueDate = new_date
        #adds a new line to the compelete var when done
        if new_line == True:
            complete += "\n"
        '''puts the new edited task in string format'''
        new_task_edited = f"{taskUser}, {taskName}, {taskDes}, {dueDate}, {daysDate}, {complete}"
        old_task = taskList[index]
        task_index = 0
        '''loops through the list of tasks and checks if the old task is in the list, and if it is it rewrites the old task to the 
        new task variable'''
        for i in taskList:
            if old_task == i:
                taskList[task_index] = new_task_edited
            '''the counter loops through the list to check for the old task'''
            task_index += 1
        '''rewrites the old task with the new task'''
        with open("tasks.txt", "w") as new_data:
            new_data.writelines(taskList)

# exit function
'''this exit function exits the code and then loops through
to see if there are any blank lines and removes them '''
def exit1():
    print('Goodbye!!!')
    file2 = open("tasks.txt", "a")
    import sys
    output = ""   #looked up online how to do this
    with open("tasks.txt", "r+") as fy:
        for l in fy:
            if not l.isspace():
                '''writes new output to the empty string'''
                output += l
    fy = open("tasks.txt", "w")
    '''writes to the file the striped output'''
    fy.write(output)
    '''exits the program'''
    exit()

# statistics function
def stats():
    '''this if statement checks to see if the file useroverview and taskoverview exits as this stats function will not run without it'''
    if os.path.exists("user_overview.txt") != True and os.path.exists("task_overview.txt") != True:
        '''if the statement is true it generates reports first and then runs the below code'''
        generate_reports()

    file2 = open("tasks.txt", "r")
    file = open("user.txt", "r")

    '''opens the user_overview and task_overview file and reads from it'''
    tasksFile = open("user_overview.txt", "r")
    userFile = open("task_overview.txt", "r")

    '''reads the lines in the tasks file'''
    taskLines = tasksFile.readlines()
    userLines = userFile.readlines()

    '''gets the total task read from the files'''
    with open("tasks.txt", "r") as fp:
        '''gets the length of all the files'''
        x = len(fp.readlines())
        print('Total tasks:', x)

    '''gets the total users in the file'''
    with open("user.txt", "r") as fa:
        '''gets the length of all the lines meaning how many users are in the file'''
        lUsers = len(fa.readlines())
        print(f'''total users: {lUsers}
    ''')
    print("User overview")

    '''loops through all the lines in task lines file'''
    for line in taskLines:
        '''strips the spaces then split the lines'''
        line = line.strip("\n")
        line = line.split(",")
        line = str(line)
        '''displays the data from the file'''
        print(str(line))

    '''prints a space'''
    print("\n")

    print("Task overview")

    '''reads through the user over view file'''
    for van in userLines:
        '''strips the new line and splits it with a comma'''
        van = van.strip("\n")
        van = van.split(",")
        '''prints the data from the file'''
        print(str(van))

#generate reports function creates the data seen in display statistics
def generate_reports():
    '''open the files needed to run the function'''
    task_overview = open("task_overview.txt", "w")
    task_file = open("tasks.txt", "r")

    '''read lines in the task file'''
    lines = task_file.readlines()
    '''gets the date time '''
    import datetime
    '''counter for different totals'''
    t = 0
    c = 0
    u = 0
    o = 0
    uo = 0
    '''gets total tasks as in display stats'''
    with open("tasks.txt", "r") as fp:
        x = len(fp.readlines())
        #print('Total tasks:', x)
    '''for loop loops through the line in the file and if the conditions is met the counter
    gets added on to'''
    for line in lines:
        temp = line.split(",")
        t += 1
        #print(t)
        '''temp -1 being the end of the line in the file containing the yes or no data'''
        '''if yes , add to counter'''
        '''elif no , add to no counter'''
        if temp[-1].strip() == "yes":
            c += 1
            #print("completed tasks {}".format(c))

        elif temp[-1].strip() == "no":
            u += 1
            #print("incomplete tasks {}".format(u))

    '''today variable being the current date'''
    today = datetime.datetime.today()
    #count_overdue = 0
    '''open tasks file and readlines '''
    with open("tasks.txt", "r") as infile:
        taskLines = infile.readlines()

        '''loops through the task file using i'''
        for i in taskLines:

            '''lines variable is equal to the lines in the task file stripped by the new line and splited with a comma'''
            lines = i.strip().split(", ")

            '''the if statements checks to see if tasks is over due and incomplete if yes it adds to the counter'''
            if datetime.datetime.strptime(lines[3], "%d %B %Y") < today and lines[-1] == "no":
                '''adds to the overdue and undone counter'''
                uo += 1

            '''and if the task date is less than the current date it adds to the overdue counter'''
            if datetime.datetime.strptime(lines[3], "%d %B %Y") < today:
                o += 1
    '''formula for the incomplete tasks'''
    pi = (u / x) * 100
    #print(f"{round(pi)}% of tasks are incomplete")
    '''formula for the overdue tasks'''
    po = (o / x) * 100
    #print(f"{round(po)}% of tasks is overdue \n")
    '''tells the user howmuch tasks is over due'''
    #print(f"{uo} task is  incomplete and overdue")

    '''writes the results to the overview file in a user friendly manner '''
    task_overview.write(f'''
Total tasks {x}
Completed Tasks {c}
incomplete tasks {u}
{uo} task is incomplete and overdue
{pi}% of tasks is incomplete
{po}% of tasks is overdue''')
    task_overview.close()
    task_file.close()

    '''section 2'''
    '''opens the files needed being user.txt, tasks.txt, and creates user overview.txt'''
    user_overview = open("user_overview.txt", "w")
    task_file = open("tasks.txt", "r")
    #user_file = open("user.txt", "r")
    #user_overview = open("user_overview.txt")
    '''reads lines within these files'''
    #linesUser = user_file.readlines()
    linesTask = task_file.readlines()


    '''total tasks generated as seen in display stats'''
    with open("tasks.txt", "r") as fp:
        x = len(fp.readlines())
        print('Total tasks:', x)

    '''total users generated as seen in display stats'''
    with open("user.txt", "r") as fa:
        lUsers = len(fa.readlines())
        print(f'''total users: {lUsers}
    ''')


    #counts for all the different data that needs to be stored

    tu = 0
    ut = 0
    ct = 0
    uo = 0
    '''move = None'''
    '''loops through the task file'''
    for line in linesTask:
        temp = line.split(", ")

        '''counts how many tasks the logged in user has'''
        if userName == temp[0]:
            tu += 1
            '''move = True'''
            '''if statement reads the completed and not completed tasks and adds it to the counter'''
            if temp[-1].strip() == "yes":
                ct += 1
            elif temp[-1].strip() == "no":
                ut += 1

        '''check for overdue and undone tasks'''
        dueDate = datetime.datetime.strptime(temp[3], "%d %B %Y")

        if dueDate < today and temp[-1] == "no":
            uo += 1
    #try function is used for when their is a division by zero error
    #this function was tought to us in the next modulue therefore this is my own knowledge
    try:
            '''formulas for the different percent results'''
            '''user tasks percentage'''
            ptu = tu / x * 100
            '''percentage of user completed tasks'''
            put = ut / tu * 100
            '''percentage of uncomplete tasks'''
            pct = ct / tu * 100
            '''percentage of undone and uncomplete tasks'''
            puo = uo / tu * 100


            percentUserTasks = ptu
            percentUserComplete = pct
            percentUserUncomplete = put
            percentUncompleteOverdue = puo


            '''writes the data to the file in a user friendly easy to read manner'''

            user_overview.write(f'''
Total number of registered users: {lUsers}
Total tasks generated and tracked: {x}
the total number of tasks for {userName} is: {tu}
Percentage of total tasks assigned to {userName}: {percentUserTasks}%
Percentage of tasks assigned to user that must still be completed and are overdue: {percentUncompleteOverdue}%
Percentage of tasks assigned to user that are complete: {percentUserComplete}%
Percentage of tasks assigned to user that must still be completed: {percentUserUncomplete}%''')

            #user_overview.close()
            #user_file.close()
            #task_file.close()

    #if no tasks are assigned to a user you will encounter a error of ZeroDivisionError this is break the program thats why this except is used
    except ZeroDivisionError:
        user_overview = open("user_overview.txt", "w")
        task_file = open("tasks.txt", "r")
        user_overview.write("this user has no data ")

    #and finally is used to close the file off and write to the file when either of these try or except is triggered
    finally:
            user_overview.close()
            task_file.close()
            print("Reports have been generated click 's' to view statistics ")
            print()
# ====Login Section====
file = open("user.txt", "r+")
file2 = open("tasks.txt", "r+")
'''name list and password list stores the names and passwords read from the file in a easy to read manner'''
nameList = []
passwordLIST = []
'''checkUser checks if the user name is in the file'''
lines = file.readlines()
for line in lines:
    '''strips new line and splits each word with ,'''
    temp2 = line.strip()
    temp2 = temp2.split(", ")
    '''adds the first word in the file being the name to the name list'''
    nameList.append(temp2[0])
    '''adds the second word in the file being the password to the password list'''
    passwordLIST.append(temp2[1])

'''user inputs there name and passoword'''
userName = input("enter username: ")
password = input("enter password: ")
login = False
'''if its not in the file prompt the user to try again'''
while not login:
  '''if statement checks to see if the names and passwords match in the password and name list'''
  if userName not in nameList or password not in passwordLIST:
    print("username and password incorrect")
    userName = input("enter username: ")
    password = input("enter password: ")
    login = False
    '''user = userName + ", " + password'''
  else:
    login = True
print("access granted Welcome {}".format(userName))
file.close()
file2.close()
'''if user name in file give the menu'''
# Admin menu
while True:
  if userName == "admin":

    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
s - statistics
e - Exit
: ''').lower()
# Regular user menu
  else:
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
s - display statistics
gr - generate reports
e - Exit
: ''').lower()

# register user
  '''if the admin is logged in call the reg function'''
  if menu == 'r':
    if userName == "admin":
        reg_user()

    else:   # if user not admin display this message
            print("Sorry only admins can register new users :( ")
            pass

    '''if a is selected call the add function'''
  elif menu == 'a':
    add_task()
    pass

    '''if va is selected call view all function'''
  elif menu == 'va':
    view_all()
    pass

    '''if vm is selected call view mine function'''
  elif menu == 'vm':
    view_mine()
    pass

    '''calls exit1 function'''
  elif menu == 'e':
    exit1()
    '''calls stats function'''
  elif menu == "s":
    stats()
    '''generates reports once gr is selected'''
  elif menu == "gr":
    generate_reports()

  else:
        print("You have made a wrong choice, Please Try again")

