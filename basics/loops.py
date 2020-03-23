monday_temps = [9.1, 8.3, 6.7, 7.5, 8.7]
avg_temp = 0.0
for temperatures in monday_temps:
    avg_temp = avg_temp + temperatures

avg_temp = avg_temp / len(monday_temps)

#print(avg_temp)

username = ''

#while username != "test":
#    username = input("Enter username: ")



str_input = ''
while True:
    newline = input("Say something: ")
    if(newline != "\end"):
        str_input = str_input + " " + newline
    else:
        break
#print(str_input)



data = [99, 'no data', 95, 94, 'no data']
def foo(data):
    return [i for i in data if isinstance(i, int)]
        
print(foo(data))