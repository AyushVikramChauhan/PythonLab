import re
text = input("Enter a String : ")
pattern = input("Enter a Pattern to Match : ")

result = re.match(pattern, text)
if result:
    print("Match found at the beginning")
    print("Match text:", result.group())
else:
    print("No match found at the beginning.")