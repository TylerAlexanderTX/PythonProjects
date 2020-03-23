student_grades = [9.1, 8.8, 5.5]

mysum = sum(student_grades)

length = len(student_grades)

mymean = mysum/length
#print(mean)

def mean(mylist):
    mysum = sum(mylist)
    mylen = len(mylist)
    return mysum/mylen

#print(mean(student_grades))

def weather(temperature):
    if(temperature > 70):
        return "It is nice outside"
    else:
        return "You might want a jacket"

#input("Enter temperature: ")
#print(weather())

firstname_input = input("Enter your firstname: ")
lastname_input = input("Enter your lastname: ")


out_msg = "Hello %s %s" % (firstname_input, lastname_input)
out_msg2 = f"Hello {firstname_input} {lastname_input}"
#print(out_msg)
print(out_msg2)