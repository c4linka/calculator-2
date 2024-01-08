print("Choose digit from 1 to 4 to start calculating ") 
choice = input("1 - MULTIPLICATION, 2 - DIVISION, 3 - ADDITION, 4 - SUBSTRATION ")
if (choice != "1" or "2" or "3" or "4"):
    print("Choose from 1 to 4") #some action to be back for input of choice should be here
    

a = int(input("Write fist number "))
b = int(input("Write second number ")) 

if (choice == "1"):
    print("a*b=",(a * b))

elif (choice == "2"): #I added by myself seconf input for b if b was = 0.
        if (b == 0):
            b = int(input("Do not divide by zero! Use number different then 0. "))
            if (b != 0):
                print("a:b=",(a / b))
        else: print("a:b=",(a / b))
elif (choice == "2"):
    print("a+b=",(a + b))
elif (choice == "4"):
    print("a-b=",(a - b))
else:
    print("Choose form 1 to 4")
#I can see that last line is to far... it should be just below choice. Lesson showed like this.
"""So i added >if<, but I believe, I have to small knowlege to make it working wright right now, I will
be back to this after some more lessons ;)"""
