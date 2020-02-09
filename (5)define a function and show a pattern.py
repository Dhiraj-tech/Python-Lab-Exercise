#write a function called show_stars and if the rows is 5(draw a pattern(*))
rows=5
def show_stars(rows):
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
show_stars(rows)
