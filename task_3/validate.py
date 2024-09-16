def user_details():
    display_list = []
    
    name = input("Enter name here: ")
    if len(name) < 2 or len(name) > 64:
        print("Incorrect details re-enter")
        user_details()

    age = int(input("Enter age here between 16 to 30: "))
    if age < 16 or age > 30:
        print("Incorrect details re-enter")
        user_details()

    department = input("Enter your department here: ")
    if not department.isalpha():
        print("Incorrect details only Alphabets are allowed")
        user_details()

    reg_no = input("Enter reg number here XXXX/YYYYYY: ")
    if "/" not in reg_no:
        print("Incorrect details missing symbols /")
        user_details()
    
    display_list.insert(0, name) 
    display_list.insert(1, age)
    display_list.insert(2, department)
    display_list.insert(3, reg_no)

    print("The user name is ",display_list[0])
    print("The user age is ",display_list[1])
    print("The user department is ",display_list[2])
    print("The user reg_no is ",display_list[3])


user_details()