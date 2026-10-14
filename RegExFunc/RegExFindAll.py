import re
text = input("Enter a String : ")
pattern = input("Enter a Pattern : ")
result = re.findall(pattern, text)
if result:
    print("Pattern found in the string.")
    print("Matched texts :", result)
    print("Number of matches found :", len(result))
else:
    print("Pattern not found in the string.")