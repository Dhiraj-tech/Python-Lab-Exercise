salary=int(input("enter a yearly salary"))
if salary <=400000:
    print("1% tax in salary")
elif salary >400000 and salary <600000:
    print("5% tax in salary")
elif salary >600000 and salary <900000:
    print("10% tax in salary")
elif salary >=900000:
    print("35% tax in salary")
