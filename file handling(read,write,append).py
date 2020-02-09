s=open("dhiraj.txt","w")
s.write("I want to be a great programmer:")
s.close()
s=open("dhiraj.txt","r")
print(s.read())
s.close()

s=open("dhiraj.txt","a")
s.write("I luv Artificial Intelligence")
s.close()

s=open('dhiraj.txt','r')
print(s.read())
s.close()
