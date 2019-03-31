a = int(input())
x = True
for i in range(2, a):
   if a%i == 0:
       x = False
       break
if x:
    print ("Простое")
else:
    print ("Не простое")
