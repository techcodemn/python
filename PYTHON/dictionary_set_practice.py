# Create a dictionary with student names and marks.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}



# Access a dictionary value by key.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}
print(student["name"])


# Add a new key-value pair.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}
student["age"]=32

print(student)

# Update an existing key.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

student["marks"]=[45,85,74,98]
print(student)

# Remove a key using del.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

del student["marks"]
print(student)


# Remove a key using pop().


student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

student.pop("marks")
print(student)


# Iterate over keys.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

for key in student:
    print(key,student[key])


# Iterate over values.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

for values in student:
    print(values,student[values])



# Iterate over key-value pairs using .items().

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

for key ,values in student.items():
    print(key,"",values)




# Check if a key exists using in.

student={
    "name":"aman",
    "marks":[95,77,75,78,]

}

print("roll"in student)


# Count frequency of characters in a string using dictionary.

cha= input("enter the string :-")
count={}

for ch in cha:
    if cha in count:
        count[ch] +=1
    else:
        count[ch]=1
        print(count)

# Count frequency of words in a sentence.

cha= input("enter the sentence :-")
word=cha.split()
count={}
for ch in word:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)

#Group words by their first letter using dictionary.
 

words=["aman","samkar","apple","shiva"]
group={}
for word in words:
    
    first=word[0]
    if first not in group:
        group[first]={}
    group[first].append(word)
print(group)
    

# Find max mark and student name.

students = {
    "Aman": 85,
    "Rahul": 92,
    "Shiva": 78,
    "Riya": 88
}

max_student = max(students, key=students.get)
print("Student:", max_student)
print("Marks:", students[max_student])
# Find student with lowest mark.

students = {
    "Aman": 85,
    "Rahul": 92,
    "Shiva": 78,
    "Riya": 88
}

min_student = min(students, key=students.get)
print("Student:", min_student)
print("Marks:", students[min_student])
# Create dictionary from two lists (keys list and values list).

keys = ["A", "B", "C", "D"]
values = [10, 20, 30, 40]

data = dict(zip(keys, values))
print(data)
# Merge two dictionaries (second overwrites).

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 5, "c": 3}

merged = dict1 | dict2
print(merged)
# Merge two dictionaries (combine values into list—custom).

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 5, "c": 3}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    if key in result:
        result[key] = [result[key], dict2[key]]
    else:
        result[key] = dict2[key]

print(result)
# Create a set from a list and print unique values.

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique = set(numbers)
print(unique)
# Remove duplicates from list using set.

numbers = [1, 2, 3, 2, 4, 5, 1, 6]

numbers = list(set(numbers))
print(numbers)
# Add elements to a set using add().

items = {1, 2, 3}

items.add(4)
items.add(5)

print(items)
# Remove elements from a set using discard().

items = {1, 2, 3, 4, 5}

items.discard(3)
items.discard(10)

print(items)
# Check membership in a set.

items = {10, 20, 30, 40}

value = 20

if value in items:
    print("Present")
else:
    print("Not Present")
# Compute set union.

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)
# Compute set intersection.

A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)
# Compute set difference (A-B).

A = {1, 2, 3}
B = {3, 4, 5}

print(A - B)
# Compute symmetric difference.

A = {1, 2, 3}
B = {3, 4, 5}

print(A ^ B)
# Use set to find common elements between two lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1) & set(list2)

print(common)
# Use set to find elements present in one list only.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

only = set(list1) - set(list2)

print(only)
# Build a dictionary where keys are numbers and values are their squares.

numbers = [1, 2, 3, 4, 5]

square = {}

for num in numbers:
    square[num] = num ** 2

print(square)
print("thank you aman")