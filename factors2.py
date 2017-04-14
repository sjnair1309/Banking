Numbers= raw_input('Enter a list of numbers:')
num=Numbers.strip().split(',')
print Numbers
for x in num:
 mylist=[]
 i=0
 x=int(num[i])
 for i in range(1, x-1):
  if x%i == 0:
   mylist.append(i)
   i=i+1
print mylist
