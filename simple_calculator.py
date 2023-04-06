#%%
#hw#2의 내용을 구현
def arithmetic_ops(op):
    num1 = int(input("Input 1st number:"))
    num2 = int(input("Input 2nd number:"))
    return num1, sum2, op(num1, num2)
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
while True:
    op = input("Input operation:")
    if op == "end":
        break
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add)
    
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x, y:x*y)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x,y: x/y)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x, y: x%y)

    else:
        print("Invalid operation")
        continue
    print(f"{num1}{op}{num2} = {ret}")

print("Exit program")