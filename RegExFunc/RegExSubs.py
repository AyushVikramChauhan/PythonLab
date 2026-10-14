import re
text = input("Enter a String : ")
pattern = input("Enter a Pattern that you want to replace : ")
replacement = input("Enter the Replacement String : ")

result = re.sub(pattern, replacement, text)
print("Original String is :", text)
print("Modified String is :", result)