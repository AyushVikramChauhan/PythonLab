import re
text = input("Enter a String : ")
pattern = input("Enter a Pattern to Match : ")
result = re.search(pattern, text)
if result:
    print("Pattern found in the string.")
    print("Match text :", result.group())
else:
    print("Pattern not found in the string.")