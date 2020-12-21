#This program takes 5 input from user and prints to console their Values and Types.

counter = 1
values = list()
while (counter < 6):
    value = input("Please give {}. value : ".format(counter))
    values.append(value)
    counter += 1

counter = 1
for val in values:
    print("Your {}. value is {} and its type is : {}".format(counter, val, type(val)))
    counter += 1

