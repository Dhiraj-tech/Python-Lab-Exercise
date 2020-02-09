# Maintain Hierarchy in a exception handling
try:
    print(10/0)
except ArithmeticError:
    print("ArithmeticError")
except ZeroDivisionError:
    print("ZeroDivisionError")
