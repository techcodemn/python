# ARITHMETIC OPERATIONS
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The sum of two numbers is: {num1 + num2}")
print("The difference of two numbers is:", num1 - num2)
print("The product of two numbers is:", num1 * num2)
print("The quotient is:", num1 / num2)
print("The remainder is:", num1 % num2)
print("The power is:", num1 ** num2)

# RELATIONAL OPERATORS
print("num1 is equal to num2:", num1 == num2)
print("num1 is not equal to num2:", num1 != num2)
print("num1 is greater than num2:", num1 > num2)
print("num1 is less than num2:", num1 < num2)
print("num1 is greater than or equal to num2:", num1 >= num2)
print("num1 is less than or equal to num2:", num1 <= num2)

# ASSIGNMENT OPERATORS
base = num1

num1 = base
num1 = num2
print("After num1 = num2:", num1)

num1 = base
num1 += num2
print("After num1 += num2:", num1)

num1 = base
num1 -= num2
print("After num1 -= num2:", num1)

num1 = base
if num2 != 0:
    num1 /= num2
    print("After num1 /= num2:", num1)
else:
    print("Cannot divide by zero")

num1 = base
if num2 != 0:
    num1 %= num2
    print("After num1 %= num2:", num1)
else:
    print("Cannot modulo by zero")

num1 = base
num1 **= num2
print("After num1 **= num2:", num1)

num1 = base
if num2 != 0:
    num1 //= num2
    print("After num1 //= num2:", num1)
else:
    print("Cannot floor divide by zero")

# BITWISE OPERATORS (ONLY FOR INTEGERS)
num1 = base

if isinstance(num1, int) and isinstance(num2, int):
    print("After num1 &= num2:", num1 & num2)
    print("After num1 |= num2:", num1 | num2)
    print("After num1 ^= num2:", num1 ^ num2)
    print("After num1 >>= num2:", num1 >> num2)
    print("After num1 <<= num2:", num1 << num2)
else:
    print("Bitwise operations only work with integers")

# LOGICAL CHECK
print("num1 < num2 < 0:", num1 < num2 < 0)

# LOOP FIX
m = 5
for i in range(4):
    print("h")