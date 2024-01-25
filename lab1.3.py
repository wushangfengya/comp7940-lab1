l = [52633, 8137, 1024, 999]
for n in range(len(l)):
    for i in range(1,l[n]+1):
         if l[n]%i==0:
             print(i,end=" ")