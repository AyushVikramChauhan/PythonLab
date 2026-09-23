def change_string(s):
    s="x"+s[1:]
    print("Inside the funciton string is:",s)

s= input("Enter a string:")
print("Before the function:",s)

change_string(s)
print("Outside the functiuon:",s)