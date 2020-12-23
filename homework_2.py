print("Welcome this program, please enter your informations")

first_name = input("First Name : ")
last_name = input("Last Name : ")
age = int(input("Age : "))
birth_date = input("Date Of Birth (just year) : ")

person_info = [first_name, last_name, age, birth_date]

for info in person_info:
    print(info)

if (person_info[2] < 18):
    print("You can't go out because it's too dangerous!")
else:
    print("You can go out to street.")
