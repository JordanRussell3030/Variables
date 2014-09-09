#Jordan Russell
#09/09/14
#First python program

#print statement displays the exact text enclosed in the speech marks and brackets.
#first_name is a variable stored as whatever is input as the variable e.g first_name could be stored as Jordan, so when asked to print the input it will retrieve Jordan. It can be changed to anything else.
#.format tells the computer to retrieve the variable from the memory.

print("Hello world")
first_name = input("Please enter your name: ")
print(first_name)
print("Hi {0}".format(first_name))
