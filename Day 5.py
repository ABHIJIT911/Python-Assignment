# Day 5 Assignment : Use filter function to filter out the elements from a list that are divisible by 3 & 5

li = list(range(1,201))
  
r3 = list(filter(lambda x: (x % 3 == 0), li)) 
r5 = list(filter(lambda x: (x % 5 == 0), li)) 
  
print("The number only divisible by 3 in 1-200 number :",r3) 
print("\nThe number only divisible by 5 in 1-200 number :",r5)