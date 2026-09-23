def remove_last(lst):
    lst.pop()
n=int(input("Enter the numbers of elements."))
lst=[]
for i in range(n):
    x=int(input("Enter the element:"))
    lst.append(x)
#lst = list("Enter the elements of the list ")
#lst= list(map(int,lst.split()))

print("Original List before Mutation",lst)
remove_last(lst)
print("Mutated List ", lst)


