
def print_menu():
    print("""Choose a number: 
    1. Veiw all projects
    2. Create a project
    3. Delete a project
    4. Edit a project
    0. QUIT""")


import projectSDK
from project import Project

print("Hello, Welcome to your Crowd-Funding.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        print("Here are all of your projects:")
        for project in projectSDK.get_projects():
            print(project)
    elif response == 2:
        print("Title?")
        title = input()
        print("Details?")
        details = input()
        print("Total Target?")
        total_target = input()
        print("Start Time?")
        start_time = input("Start Date (mm/dd/yyyy) : ")
        print("End Time?")
        end_time = input("End Date (mm/dd/yyyy) : ")
        projectSDK.add_project(Project(title,details,total_target,start_time,end_time))
    elif response == 3:
        print("Title?")
        title = input()
        print("Details?")
        details = input()
        print("Total Target?")
        total_target = input()
        print("Start Time?")
        start_time = input("Start Date (mm/dd/yyyy) : ")
        print("End Time?")
        end_time = input("End Date (mm/dd/yyyy) : ")
        projectSDK.delete_project(Project(title,details,total_target,start_time,end_time))
    elif response == 4:
        print("Current title?")
        current_title = input()
        print("Current details?")
        current_details = input()
        print("Current Total Target?")
        current_total_target = input()
        print("Current Start Time?")
        current_start_time = input("Start Date (mm/dd/yyyy) : ")
        print("Current End Time?")
        current_end_time = input("End Date (mm/dd/yyyy) : ")
        print("New title (s for same)")
        new_title = input()
        if str.lower(new_title) == 's':
            new_title = current_title
        print("New details? (s for same)")
        new_details = input()
        if str.lower(new_details) == 's':
            new_details = current_details
        print("New total target? (s for same)")
        new_total_target = input()
        if str.lower(new_total_target) == 's':
            new_total_target = current_total_target
        print("New start time? (s for same)")
        new_start_time = input("Start Date (mm/dd/yyyy) : ")
        if str.lower(new_start_time) == 's':
            new_start_time = current_start_time
        print("New end time? (s for same)")
        new_end_time = input("End Date (mm/dd/yyyy) : ")
        if str.lower(new_end_time) == 's':
            new_end_time = current_end_time
        projectSDK.update_project(Project(current_title, current_details,current_total_target,current_start_time,current_end_time), new_title, new_details,new_total_target,new_start_time,new_end_time)
    else:
        print("Good luck!")
        break