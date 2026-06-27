# # Taking a string input and printing it in uppercase:-
# name=input("enter any name in lowercase:-")
# print(name.upper())
 



# # Taking a string input and printing it in lowercase:-

# name=input("enter any name in uppercase:-")
# print(name.lower())

# # Check if a string contains the letter 'a'.
# name=input("enter any name in lowercase:-")
# if name.count("a")>0:
#     print("a is avilable")
#     print(name.count("a"))
# else:
#     print("not avilable a")

   
# # Check if a string starts with "py".

# text=input("enter any string which start from py:-")
# if text.startswith("py"):
#     print("yes it's with py")
# else:
#     print("not start with py")


# # Check if a string ends with "on".

# text=input("enter any string and check its end with on or not:-")
# if text.endswith("on"):
#     print("oh yes! its end with on")
# else:
#     print("so sad not ending with on")


# # Print the number of characters in a string.
# character=input("enter any string:-")
# print(len(character))


# # Print the first 3 characters.
# character=input("enter any string:-")
# print(character[0:3])


# # Print the last 3 characters.

# character=input("enter any string:-")
# print(character[0:3])

# # Print characters at even indices.

# character=input("enter any string:-")
# print(character[::2])


# # Print characters at odd indices.

# character=input("enter any string:-")
# print(character[1::3])

# # Reverse a string using slicing.

# character=input("enter any string:-")
# print(character[::-1])

# Reverse a string using slicing.
# text=input("enter any string:-")
# reverse=""
# for i in text:
#     reverse=i+reverse
# print(reverse)

# Count vowels in a string.


# ch=input("enter any string:-")
# count=0
# for i in ch:
#     if i in "aeiouAEIOU":
#         count +=1
# print(count) 
      



# # Count consonants in a string.
# text=input("enter any string")
# count=0
# for i in text:
#     if i.isalpha() and i not in("aeiou"):
#         count+=1
# print(count)

 

# ch=input("enter any string:-")
# print(ch.count("a,e,i,o,u")) 

# Remove spaces from a string.

# text=input("enter any string")
# print(text.replace(" ",""))

# Replace all spaces with -.

# text=input("enter any string")
# print(text.replace(" ","-"))

# # Replace a given substring with another substring.
# text=input("enter any string")
# text2=input("enter any string")
# print(text.replace(" text","text2"))

# # Split a sentence into words and print the list.
# text=input("enter any string")
# print(text.split())


# # Join a list of words into a sentence.
# text=["aman","is", "python","developer"]
# print(" ".join(text))

# # Use strip() to remove leading/trailing spaces.
# text=input('"enter any string"')
# print(text.strip())

# Use lstrip() and rstrip() separately.


# text=input("enter any string :-")
# print(text.lstrip())
# print(text.rstriptrip())

# # Convert string to title case.
# text=input("enter any string to title case:-")
# print(text.title())

# # Convert string to capitalize case.


# text=input("enter any string for Convert string to title case :-")
# print(text.capitalize())
 

# # Check if string is palindrome.


# text="amna"
# print("string is palindrome")

# if text==text[::-1]:
#   print("is palindrome")
# else:
#    print('not palindrome')


# Check if string is an anagram of another string (simple version: lowercase compare sorted chars).


# text1=input("enter any string :-")
# text2=input("enter any string :-")
# if sorted(text1.lower()) == sorted(text2.lower()):
#     print("it is anagram")
# else:
#     print("not anagram")


# # Count occurrences of a character in a string.

# text1=input("enter any string :-")
# text2=input("enter occurance charchter:-")
# print(text1.count(text2))

# # Find index of a substring.

# text1=input("enter any string :-")
# text2=input("enter index word :-")
# print(text1.find(text2))


# # Count occurrences of a substring.

# text1=input("enter any string :-")
# text2=input("enter index word :-")
# print(text1.count(text2))

# # Use find() to locate a character.

# text1=input("enter any string :-")
# text2=input("enter locate character :-")
# print(text1.find(text2))

# Use index() and handle error conceptually.

# text1=input("enter any string :-")
# text2=input("enter substring :-")
# try:
#     print("value NOT found")
# except ValueError:
#     print (" found")

# # Extract a substring using slicing.

# text1=input("enter any string :-")
# text2=int(input("enter start index :-"))
# text3=int(input("enter endex :-"))
# print(text1[text2:text3])


##  Extract substring from index i to end.
 

# text1=input("enter any string :-")
# i=int(input("enter start index :-"))
# print(text1[i:])


# # Extract substring from start to index j.


# text1=input("enter any string :-")
# j=int(input("enter start index :-"))
# print(text1[:j])


# # Convert numeric string to int and do arithmetic.

# a=int(input("enter a string :-"))
# b=int(input("enter a string :-"))
# sum=a+b
# sub=a-b
# multi=a*b
# div=a/b
# print(f"the sum{sum},{sub},{multi},{div}")

# # Use isdigit() to check if input is numeric. 

# a=(input("enter a string :-"))
# print(a.isdigit())

# # Use isalpha() to check if string has only letters.

# a=input("enter a string :-")
# print(a.isalpha())

# # Use isalnum() to check alphanumeric.

# a=input("enter a string :-")
# print(a.isalnum())

## Use isspace() to check empty/space-only string.

# a=input("enter a string :-")
# print(a.isspace())

# # Make a “username validator” using conditions: length >= 5 and alphanumeric.

# a=input("enter a username :-")

# if len(a)>=5 and a.isalnum():
#     print("valid")
# else:
#     print("not valid")


# Make a password validator with basic rules (length >= 8).

a=input("enter a password :-")

if len(a)>=8 and all(ch.isalnum() or ch=='@'for ch in a):
    print("valid")
elif len(a)<=8:
    print("enter password of 8 usinig alpha,numric,special charachter")
else:
    print("done")
print("thank u to login")
