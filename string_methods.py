a= "rahim"

print(a)
print(a.title())
#(title method is used to capitalize the first character of a string and rest of the characters are in lower case.)

print(a.upper())
#(upper method is used to convert all the characters of a string into upper case.)

print(a.lower())    
#(lower method is used to convert all the characters of a string into lower case.)

print(a.capitalize())
#(capitalize method is used to capitalize the first character of a string and convert the rest of the characters into lower case.)

print(a.swapcase()) 
#(swapcase method is used to convert all the uppercase characters into lowercase and all the lowercase characters into uppercase.)

print(a.replace("rahim","nazifa"))
#(replace method is used to replace a substring with another substring.)

print(a.replace("rahim","nazifa").upper())
#(first replaces the substring, then converts to upper case.)

print(a.replace("rahim","nazifa").lower())  
#(first replaces the substring, then converts to lower case.)

print(a.replace("rahim","nazifa").capitalize()) 
#(first replaces the substring, then capitalizes the first character of the string.)

print(a.replace("rahim","nazifa").swapcase())   
#(first replaces the substring, then swaps the case of all characters.)

print(a.replace("rahim","nazifa").title())  
#(first replaces the substring, then converts it to title case.)

print(a.replace("rahim","nazifa").replace("nazifa","rahim"))
#(first replaces "rahim" with "nazifa", then replaces "nazifa" back to "rahim".)

b= "My name is Turna.I'm a student of computer science."

c= b.replace('Turna','Nazifa').replace('computer science','computer science & engineering')

print(b)
print(c)
