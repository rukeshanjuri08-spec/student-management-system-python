import json
#------------ load data -----------------------
try:
    with open("students.json","r") as f:
        students = json.load(f)
except:
    students = []

# ----------------functions (define first)---------------

def save_data():
    with open("students.json","w") as f:
        json.dump(students,f)

def add_student(students):
    id = input("enter id:")
    
    if not id.isdigit():
        print("id must be number")
        return
    
    for s in students:
        if s["id"]==id:
            print("id already exists")
            return
        
    name = input("enter name:")

    if name.strip()=="":
        print("name can't be empty")
        return
    
    student ={"id":id,"name":name}
    students.append(student)
    save_data()
    print("student added")

def view_students(students):
    if len(students)==0:
        print("no student found")
    else:
        for student in students:
            print("id:",student["id"],"name:",student["name"])

def search_student(students):
    search_name=input("enter name to search:")  
    found=False

    for student in students:
        if student["name"].lower().strip()==search_name.lower().strip():
            print(f"id:{student['id']}|name:{student['name']}")
            found=True

    if not found:
        print("not found")

def delete_student(students):
    delete_name=input("enter name to delete:")
    found=False

    for student in students:
        if student["name"].lower().strip()==delete_name.lower().strip():

            confirm = input("are you sure?(yes/no):")
            if confirm.lower() !="yes":
                return
            
            students.remove (student)
            save_data()
            print("deleted")
            found=True
            break
           
        if not found: 
            print("not found")

def update_student(students):
    update_id=input("enter id to update:")
    found=False

    for student in students:
        if student["id"]==update_id:
            new_name=input("enter new name:")

            if new_name.strip()=="":
                print("name can't be empty")
                return
            
            student["name"]=new_name
            save_data()
            print("updated")
            found=True
            break

    if not found:
        print("not found")

def sort_students(students):
    students.sort(key=lambda x: x["name"].lower())
    print("students shorted by name")

def count_students(students):
    print("total students:",len(students))                



#---------------main loop---------------

while True:
    print("\n--- student record system--")
    print("1.add student")
    print("2.view students")
    print("3.search student")
    print("4.delete student")
    print("5.update student")
    print("6.sort students")
    print("7.total students")
    print("8.exit")

    choice=input("enter choice:")

    if choice=="1":
        add_student(students)

    elif choice=="2":
        view_students(students) 

    elif choice=="3":
        search_student(students)

    elif choice=="4":
        delete_student(students)

    elif choice=="5":
        update_student(students) 

    elif choice=="6":
        sort_students(students)

    elif choice=="7":
        count_students(students)           

    elif choice=="8":
        print("exiting...")
        break

    else:
        print("invalid choice")       