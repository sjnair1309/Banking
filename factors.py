Numbers= raw_input('Enter a list of numbers:')
num=Numbers.strip().split(',')
print Numbers
def factors(n):
 mylist=[]
 i=0
 for i in range(1, n-1):
  if n%i == 0:
   mylist.append(i)
   i=i+1
 return mylist
p = factors(int(Numbers))
print p