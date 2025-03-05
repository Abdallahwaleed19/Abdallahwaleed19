num = int(input())
x = '7'
if (num%7!=0 and x not in str(num)):
    print(0)
elif (num%7==0 and x not in str(num) ):
    print(1)
elif (num%7!=0 and x in str(num) ):
    print(2) 
elif (num%7==0 and x in str (num) ):
    print(3)       

