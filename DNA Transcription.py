x=input()
flag=True
# print(len(x))
for l in range((len(x))):
    if (x[l]!='C') and (x[l]!='G') and (x[l]!='A') and (x[l]!='T'):
         print("Invalid Input")
         flag = False
         break
         
if flag==True:
    for l in range((len(x))):  
         if x[l] == 'C':
             print("G",end="")
         elif x[l]=='G':
             print("C",end="")
         elif x[l]=='A':
             print("U",end="")
         elif x[l]=='T':
             print("A",end="")   
    
    