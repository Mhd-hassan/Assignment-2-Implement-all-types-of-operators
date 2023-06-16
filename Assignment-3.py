# Python Assignment-3 Implement each types of operators
# Operator-1 Arithmetic 
n1=float(input("Enter the value of number one : "))
n2=float(input("Enter the value of number two : "))
ans=n1+n2 # Arithmetic Addition operator
print("The addition of two number is : ",ans)
ans=n1-n2 # Arithmetic Subtraction operator
print("The subtraction of two number is : ",ans)
ans=n1*n2 # Arithmetic Multiplication operator
print("The multiplication of two number is : ",ans)
ans=n1/n2 # Arithmetic Division operator
print("The division of two number is : ",ans)
ans=n1//n2 # Arithmetic Floor Division operator
print("The floor division of two number is : ",ans)
ans=n1%n2 # Arithmetic Modulus operator
print("The modulus of two number is : ",ans)
ans=n1**n2 # Arithmetic Exponentitation operator
print("The exponentitation of two number is : ",ans)
"""
Output of Arithmetic operator:
Enter the value of number one : 20
Enter the value of number two : 10
The addition of two number is :  30.0
The subtraction of two number is :  10.0
The multiplication of two number is :  200.0
The division of two number is :  2.0
The floor division of two number is :  2.0
The modulus of two number is :  0.0
The exponentitation of two number is :  10240000000000.0
"""
# Operator-2 Assignment
n1=10
n2=20
c=n1+n2 # Assignment Assign operator
print(c)
n1+=n2 # n1=n1+n2 Assignment Assign and Add operator
print(n1)
n1-=n2 # n1=n1-n2 Assignment Assign and Subtract operator
print(n1)
n1*=n2 # n1=n1*n2 Assignment Assign and Multiply operator
print(n1)
n1/=n2 # n1=n1/n2 Assignment Assign and Division operator
print(n1)
n1//=n2 # n1=n1//n2 Assignment Assign and Floor Division operator
print(n1)
n1%=n2 # n1=n1%n2 Assignment Assign and Modulus operator
print(n1)
n1**=n2 # n1=n1**n2 Assignment Assign and Exponentitation operator
print(n1)
n1&=n2 # n1=n1&n2 Assignment Assign and bitwise AND operator
print(n1)
n1|=n2 # n1=n1|n2 Assignment Assign and bitwise OR operator
print(n1)
n1^=n2 # n1=n1^n2 Assignment Assign and bitwise XOR operator
print(n1)
n1>>=n2 # n1=n1>>n2 Assignment Assign and bitwise Right Shift operator
print(n1)
n1<<=n2 # n1=n1<<n2 Assignment Assign and bitwise Left Shift operator
print(n1)
"""
Output of Assignment operator:
30
30
10
200
10.0
0.0
0.0
0.0
"""
# Operator-3 Comparison
n1=10
n2=10
if n1==n2: # Comparison Equal operator
    print("The value of number one and number two is equal")
n1=15
n2=20
if n1!=n2: # Comparison Not Equal operator
    print("The value of number one is not equal to number two")
n1=20
n2=10
if n1>n2: # Comparison Greater than operator
    print("The value of number one is greater than the value of number two")
n1=10
n2=15
if n1<n2: # Comparison Less than operator
    print("The value of number one is smaller than the value of number two means the value of number two is greater than the value of number one")
n1=20
n2=20
if n1>=n2: # Comparison Greater than or Equal operator
    print("The value of number one and number two are equal")
if n1<=n2: # Comparison Less than or Equal operator
    print("Both the value are equal")
"""
Output of Comparison operator:
The value of number one and number two is equal
The value of number one is not equal to number two
The value of number one is greater than the value of number two
The value of number one is smaller than the value of number two means the value of number two is greater than the value of number one
The value of number one and number two are equal
Both the value are equal
"""
# Operator-4 Logical
n=3
if n<5 and n<10: # Logical AND operator
    print(n)
if n>5 and n<10: # Logical AND operator
    print(n)
if n<5 or n<10: # Logical OR operator
    print(n)
if n>5 or n<10: # Logical OR operator
    print(n)
print(not(n<5 and n<10)) # Logical NOT operator
print(not(n>5 and n<10)) # Logical NOT operator
"""
Output of Logical operator:
3
3
3
False
True
"""
# Operator-5 Membership
x=["Apple","Mango"]
print("Mango" in x) # Membership IN operator
y=["Apple","Mango"]
print("Orange" not in y) # Membership NOT IN operator
"""
Output of Membership operator:
True
True
"""
# Operator-6 Bitwise
print(6&3) # Bitwise AND operator
print(6|3) # Bitwise OR operator
print(6^3) # Bitwise XOR operator
print(~3) # Bitwise NOT operator
print(~6) # Bitwise NOT operator
print(6<<3) # Bitwise Left Shift operator
print(6>>3) # Bitwise Right Shift operator
"""
Output of Bitwise operator:
2
7
5
-4
-7
48
0
"""
# Operator-7 Identity
x=["Apple","Banana"]
y=["Apple","Banana"]
z=x
print(x is z) # Identity IS operator
print(x is y) # Identity IS operator
print(x==y) # Identity IS operator
print(x==z) # Identity IS operator
print(y is x) # Identity IS operator
print(y is z) # Identity IS operator
print(y==x) # Identity IS operator
print(y==z) # Identity IS operator
print(x is not z)
print(x is not y)
print(x!=y)
print(x!=z)
print(y is not z)
print(y is not x)
print(y!=x)
print(y!=z)
"""
Output of Identity operator:
True
False
True
True
False
False
True
True
False
True
False
False
True
True
False
False
"""
"""
Output of all the operators:
Enter the value of number one : 20
Enter the value of number two : 10
The addition of two number is :  30.0
The subtraction of two number is :  10.0
The multiplication of two number is :  200.0
The division of two number is :  2.0
The floor division of two number is :  2.0
The modulus of two number is :  0.0
The exponentitation of two number is :  10240000000000.0
30
30
10
200
10.0
0.0
0.0
0.0
The value of number one and number two is equal
The value of number one is not equal to number two
The value of number one is greater than the value of number two
The value of number one is smaller than the value of number two means the value of number two is greater than the value of number one
The value of number one and number two are equal
Both the value are equal
3
3
3
False
True
True
True
2
7
5
-4
-7
48
0
True
False
True
True
False
False
True
True
False
True
False
False
True
True
False
False
"""