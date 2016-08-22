import math

if __name__ == "__main__":

    print("Usage: (1+((2+3)*(4*5)))")
    formula = input("Enter an equation: ")

    ops = []
    vals = []

    for i in formula:
        if i == "(":
            pass
        elif i == "+":
            ops.append(i)
        elif i == "-":
            ops.append(i)
        elif i == "*":
            ops.append(i)
        elif i == "/":
            ops.append(i)
        elif i == "sqrt":
            ops.append(i)
        elif i == ")":
            operand = ops.pop()
            value = int(vals.pop())
            if operand == "+":
                value = value + int(vals.pop())
            elif operand == "-":
                value = value - int(vals.pop())
            elif operand == "/":
                value =  value / int(vals.pop())
            elif operand == "*":
                value = value * int(vals.pop())
            elif operand == "sqrt":
                value = math.sqrt(value)
            vals.append(value)
        else:
            vals.append(i)
    print(vals.pop())
