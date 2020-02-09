# Maintain Hierarchy in a exception handling
try:
    print(10/0)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
