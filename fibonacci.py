def fibonacci(n):
   series = []
   a = 0
   b= 1
   for _ in range(n):
         series.append(a)
      
         next = a+b
      
         a= b
         b = next
   
   return series

print(fibonacci(10))
