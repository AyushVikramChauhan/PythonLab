#question 3(a)
def add_entry(d):
    key= input("Enter the key to add: ")
    value= input("Enter value to add: ")

    d["Key"]=value
def reassign_dict(d):
    d={}
    key= input("Enter the key for new dictionary to add: ")
    value= input("Enter value fro new dictionary to add: ")
    d["Key"]=value
    print("Inside the function before mutation",d)
d={}
n=int(input("Enter the number of entries to add: "))

for i in range(n):
    key = input("Enter the key to add: ")
    value = input("Enter the value to add: ")
    d[key]=value
    print("Inside the function after mutation",d)

add_entry(d)
print("After the function call inside the function",d)

reassign_dict(d)
print("After the function reassignment call inside the function",d)
