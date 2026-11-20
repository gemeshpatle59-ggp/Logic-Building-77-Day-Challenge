# Create a to-do manager using a list/dictionary with add, update, delete, complete, search, and numbering.

import json
import os

To_do = {
    "learn python" : True,
    "Hit GYM" : False
}

def load_data():
    global To_do

    if os.path.exists("To_do.json"):
        with open("To_do.json", "r") as file:
            To_do = json.load(file)

    else:
        save_data()

def save_data():
    with open("To_do.json","w") as file:
        json.dump(To_do,file,indent=4)

def Add_task(task):
    To_do[task] = False
    print("\nNew Task Is Added.")

def remove_task():
    try:
        for i ,(key , status) in enumerate (To_do.items() , start=1):
            print(f"{i}.{key} : {status}")
        n = int(input("enter task no. you want to remove.: "))
        task_list = list(To_do.keys())
        tasks = task_list[n - 1]
        To_do.pop(tasks) 
        print(f"\ntask {tasks} is removed..") 

    except ValueError:
        print("check proper numbering of tasks..")      

def Update_task():
    try:
        for i,(key,status) in enumerate (To_do.items(),start=1):
            print(f"{i}.{key} : {status}")
        n = int(input("enter task no. you want to update.: "))

        task_list = list(To_do.keys())
        tasks = task_list[n - 1]
        To_do[tasks] = True
        print("\n Task is completed..")

    except ValueError:
        print("check proper numbering of tasks")
