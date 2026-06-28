# # Create a list of 5 integers and print it. 

# number_list=[5,4,4,4,45,34,66]
# print(number_list[4])

# # Print list length.


# number_list=[5,4,4,4,45,34,66]
# print(len(number_list))


# # Access first, last elements using indices.


# number_list=[5,4,4,4,45,34,66]
# print(number_list[0])
# print(number_list[  -1])




# # Replace an element in a list.

# number_list=[5,4,4,4,45,34,66]
# number_list[3]=100
# print(number_list)




# # Add an element using append().

# number_list=[5,4,4,4,45,34,66]
# number_list.append(60)
# print(number_list)







# # Add element at a specific position using insert().


# number_list=[5,4,4,4,45,34,66]
# number_list.insert(2,60)

# print(number_list)


# # Remove element using remove().

# number_list=[5,4,4,4,45,34,66]
# number_list.remove(4)
# print(number_list)



# # Remove last element using pop().

# number_list=[5,4,4,4,45,34,66]
# number_list.pop(-1)
# print(number_list)


# # Clear a list using clear().

# number_list=[5,4,4,4,45,34,66]
# number_list.clear()
# print(number_list)

# # Create a list using range.

# number_list=list(range(1,12))
# print(number_list)

# # Create list of squares of numbers from 1 to n.

# n = int(input("Enter n: "))

# number_list = []

# for i in range(1, n + 1):
#     number_list.append(i ** 2)

# print(number_list)

# # Find max and min in a list.

# number_list=[5,4,4,4,45,34,66]

# print(max(number_list))
# print(min(number_list))



# # Sort a list ascending.

# number_list=[5,4,4,4,45,34,66]
# number_list.sort()
# print((number_list))


# # Sort descending.

# number_list=[5,4,4,4,45,34,66]
# number_list.sort(reverse=True)
# print((number_list))

# # Reverse a list using reverse().

# number_list=[5,4,4,4,45,34,66]
# number_list.reverse()
# print((number_list))


# # Copy a list correctly (shallow) and show that modifying one changes another (concept question).


# number_list = [1, 2, 3]

# copy_list = number_list

# copy_list.append(4)

# print("Original:", number_list)
# print("Copy:", copy_list)


# # Create a tuple and print it.

# text_tuple=(11,21,41,54,65)
# print(type(text_tuple))
# print(text_tuple)

## Convert a tuple to list. 

# text_tuple=(11,21,41,54,65)
# my_tuple=list(text_tuple)
# print(my_tuple)

# # Convert a list to tuple.

# text_list=[11,21,41,54,65]
# my_list=tuple(text_list)
# print(my_list)


# # Access tuple elements by index.
# text_tuple=(11,21,41,54,65)
# print(text_tuple[3])




# # Find length of tuple


# text_tuple=(11,21,41,54,65)
# print(len(text_tuple))


# # Iterate over a tuple and print elements.

# text_tuple=(11,21,41,54,65)
# for i in text_tuple:
#     print(i)

# # Create a list of strings and sort alphabetically.

# text_list=["amsn","amit","raghav","shankar","uday"]
# text_list.sort()
# print(text_list)


# # Count occurrences of a value in a list.

# text_list=[11,21,41,54,65,11,11,11]
# #text_list.count()
# print(text_list.count(11))




# # Remove duplicates from a list (using loop).

# text_list=[11,21,41,54,65,11,11,11]
# my_list=[]
# for i in text_list:
#     if i not in my_list:
#         my_list.append(i)
# print(my_list)

# # Remove duplicates from a list (using set).

# text_list=[11,21,41,54,65,11,11,11]
# print(list(set(text_list)))


# Find second largest number in list.

text_list=[11,21,41,54,65,11,11,11]

text_list=list(set(text_list))
text_list.sort()
print("second largest is:-",text_list[-2])


# Find index of a given element.

text_list = [11, 21, 41, 54, 65]

print(text_list.index(41))


# Create a 2D list (matrix) and print it.
# Add two matrices (2x2) using nested loops.
# Transpose a 2D list (swap rows/cols).
# Flatten a 2D list into 1D list.
# Given list, compute sum of elements.
# Given list, compute average.
# Given list, compute total of even elements.
# Given list, compute total of odd elements.
# Slice a list: print elements from i to j.
# Slice using step (e.g., every 2nd element).
# Tuple immutability practice: try to change tuple element (explain error).
# Compare list and tuple: check equality after converting.