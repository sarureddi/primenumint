number1=int(input())
if number1 > 1:  
   for i1 in range(2, number1): 
       if (number1 % i1) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
  
else: 
   print("no") 
