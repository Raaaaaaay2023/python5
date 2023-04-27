#1
# def power(A, B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     elif B % 2 == 0:
#         return power(A*A, B//2)
#     else:
#         return A * power(A*A, (B-1)//2)
    
# a = int(input("Enter the value of A: "))
# b = int(input("Enter the value of B: "))
# result = power(a, b)
# print(f"{a}^{b} = {result}")


#2
def sum(a, b):
    if b == 0: 
        return a
    elif a == 0:  
        return b
    else: 
        if b > 0:  
            return sum(a+1, b-1)
        else:  
            return sum(a-1, b+1)
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
result = sum(a, b)
print(f"{a}+{b} = {result}")
