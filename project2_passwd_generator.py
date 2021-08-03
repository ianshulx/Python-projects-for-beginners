import random
import array
import time 

level=int(input("Enter password Strength\n 1.WEAK\n2.GOOD\n3.STRONG\n 1/2/3::"))
AB=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ab=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

symbol= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
w=random.choice(symbol)
x=random.randint(1,10)
y=random.choice(ab)
z=random.choice(AB)
x=str(x)
 
 
l=random.choice(symbol)
m=random.randint(1,10)
n=random.choice(ab)
o=random.choice(AB)

m=str(x)

p1=(x+y+z+w)
p2=w+y+z+x
p3=w+x+y+z
p4=w+y+z+w

pp1=l+m+n+o
pp2=n+l+o+m
pp3=m+l+o+n
pp4=l+n+o+m

p5=random.choice(p1)
p6=random.choice(p2)
p7=random.choice(p3)
p8=random.choice(p4)

pp5=random.choice(pp1)
pp6=random.choice(pp2)
pp7=random.choice(pp3)
pp8=random.choice(pp4)

password=(p5+p6+p7+p8)+p1
password1=(pp5+pp6+pp7+pp8)
password3=(pp6+p8+pp7+p5)
if level==1:
        print(password)
        
if level==2:
        print(password+password1)

if level==3:
        print(password+password3)
