def factorial(num):
    facto = 1
    for i in range(1, num + 1):
        facto *= i
    return facto

def FactCheck(num):
    digits = [int(digit) for digit in str(num)]
    
    for i in range(len(digits)):
        digits[i] = factorial(digits[i])
        
    return sum(digits) == int(num)
    
f = input("enter a num: ")

print(f"{f} is factorion") if FactCheck(f) else print(f"{f} ain't factorion")