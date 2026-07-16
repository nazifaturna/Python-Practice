a= "this is a string"
print(a[0])
print(a[15]) 


 #len machine, len method is used to find the length of a string 
print(len(a))

#maximum index = length of string -1
print(len(a)-1)


#last character of string (long method)
print(a[len(a)-1])


#last character of string (short method)
print(a[-10])
 #only python can effort (-ve indexing) 
print(a[-5]) #prints 5th last character of string
 
  #string is a immutable data type, we cannot change the value of a string once it is created.
