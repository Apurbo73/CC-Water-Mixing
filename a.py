import math
n = int (input())
for _ in range (n):
    a,b,c,d = map(int,input().split())
    if a==b:
        print ("YES")
    elif a<b :
        g=b-a
        if g<=c:
            print ("YES")
        else:
            print("NO")
    elif a>b:
        h= a-b
        if h>d:
            print ("NO")
        else:
            print("YES")