# # Create a dictionary with student names and marks.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }



# # Access a dictionary value by key.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }
# print(student["name"])


# # Add a new key-value pair.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }
# student["age"]=32

# print(student)

# # Update an existing key.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# student["marks"]=[45,85,74,98]
# print(student)

# # Remove a key using del.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# del student["marks"]
# print(student)


# # Remove a key using pop().


# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# student.pop("marks")
# print(student)


# # Iterate over keys.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# for key in student:
#     print(key,student[key])


# # Iterate over values.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# for values in student:
#     print(values,student[values])



## Iterate over key-value pairs using .items().

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# for key ,values in student.items():
#     print(key,"",values)




# # Check if a key exists using in.

# student={
#     "name":"aman",
#     "marks":[95,77,75,78,]

# }

# print("roll"in student)


# # Count frequency of characters in a string using dictionary.

# cha= input("enter the string :-")
# count={}

# for ch in cha:
#     if cha in count:
#         count[ch] +=1
#     else:
#         count[ch]=1
#         print(count)

# # Count frequency of words in a sentence.

# cha= input("enter the sentence :-")
# word=cha.split()
# count={}
# for ch in word:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1
# print(count)

# Group words by their first letter using dictionary.
#  

words=["aman","samkar","apple","shiva"]
group={}
for word in words:
    
    first=word[0]
    if first not in group:
        group[first]={}
    group[first].append(word)
print(group)
    

# Find max mark and student name.
# Find student with lowest mark.
# Create dictionary from two lists (keys list and values list).
# Merge two dictionaries (second overwrites).
# Merge two dictionaries (combine values into list—custom).
# Create a set from a list and print unique values.
# Remove duplicates from list using set.
# Add elements to a set using add().
# Remove elements from a set using discard().
# Check membership in a set.
# Compute set union.
# Compute set intersection.
# Compute set difference (A-B).
# Compute symmetric difference.
# Use set to find common elements between two lists.
# Use set to find elements present in one list only.
# Build a dictionary where keys are numbers and values are their squares.