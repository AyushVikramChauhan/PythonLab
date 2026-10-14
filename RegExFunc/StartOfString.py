import re
text = input("Enter a String : ")
pattern = r"^Hello"
if re.search(pattern, text):
    print("String Starts with Hello . ")
else:
    print("String does not start with Hello.")
