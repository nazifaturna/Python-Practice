#string_replacement
a= "My name is Turna.I'm a student of computer science."
b= a.replace('Turna','Nazifa').replace('computer science','computer science & engineering')
##replace method is used to replace a substring with another substring. In this case, it replaces 'Turna' with 'Nazifa' and 'computer science' with 'computer science & engineering'.   
print(a)
print(b)


#string formatting
c=input("What is your name?")
d="Good Morning,{}. How are you?".format(c)
##format method is used to format a string by replacing the placeholders with the specified values. In this case, it replaces the placeholder {} with the value of c (the user's name).
print(d)

### long method of string formatting, where the placeholders are replaced with the specified values using the format method.

first_name_1= "Nazifa Anjum"
last_name_1= "Turna"
age_1= 23
text_1="My name is {first_name_1} {last_name_1}. I am {age_1} years old.".format(last_name_1=last_name_1,first_name_1=first_name_1, age_1=age_1) 
print(text_1)


### short method of string formatting, where the placeholders are replaced with the specified values using f-strings.

first_name_2= "Imrul Hasan"
last_name_2= "Khan"
age_2= 25
text_2=f"My name is {first_name_2} {last_name_2}. I am {age_2} years old." 
print(text_2)
