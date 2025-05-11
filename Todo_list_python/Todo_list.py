import csv
import os

with open('python.csv' ,'w', newline='') as file:
    writer = csv.writer(file)
    # file header
    writer.writerow(['Name','Age'])
    
    writer.writerow(['Zain','22'])
    writer.writerow(['Ali','23'])
    writer.writerow(['Zaheer','24'])
    
print("Sucessesfully created")    

FILENAME = 'python.csv'

def initilize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME,'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task','States'])
            
def add_task(data):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data,'Not Done'])   
        
def view_task():
    with open(FILENAME, mode='r')  as file:
        reader = csv.reader(file)   
        task = list(reader)[1:]
        if not task :
            print(" no task founded.")
        else:
            for index, (task,states) in enumerate (task, start=1):
              print(f"{index}. {task} - {states}")  
              
def delete_task(task_number):
    tasks = []
    with open(FILENAME, mode='r' ) as file:
        reader = csv.reader(file)
        tasks = list(reader)
        
    if task_number <=0 or task_number >= len(tasks):
        print(f"Error! Task number {task_number} doese not given")
        return
    
    Deleted_task = tasks.pop(task_number)
    
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
    print(f"{Deleted_task[0]} Deleted successfully.")
    
def mark_task_done(task_number):
    tasks = []
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        tasks = list(reader)
    task_number = int(task_number)
    if task_number <=0 or task_number > len(tasks):
        print(f"Error! Task number {task_number} does't given.")
        return
    task_index = task_number - 1
    task = tasks[task_index]
    task[1] = 'Done'
    
    with open(FILENAME ,mode='w' , newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
    print(f"task '{task[0]}' mark as Done") 
    
def main():
    initilize_file()
    
    while True:
        print("/n to do list menu; ")
        print("1, add task")
        print("2, view task")
        print("3, delete task")
        print("4, mark as done")
        print("5, Exit")
        
        choice = input("choose an option: ")
        
        if choice == '1':
            data = input("Enter task to add: ")
            add_task(data)  
        elif choice == '2':
            view_task()      
        elif choice == '3':
            try:
                dele = int(input("Enter task number to delete."))
                delete_task(dele)
            except ValueError:
                print(f"invaild! please enter a number.")
        elif choice == '4':
            try:
                task_done = input("Enter task to mark as done.")
                mark_task_done(task_done)
            except ValueError:
                print("please enter a vaild task number.")
        elif choice == '5':
            print("You are  Exit the game.") 
            break
        else:
            print("Invaid choice!. please try again.")
            
if __name__ == "__main__":
    main()   
            