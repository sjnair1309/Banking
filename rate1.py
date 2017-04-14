hours= raw_input("Enter no of Hours")
H= float(hours)
Rate= raw_input("Enter rate")
R= float(Rate)
if H<=40:
 pay= H*R
else:
 pay= (H-40)*R *1.5 + 40*R
print pay 