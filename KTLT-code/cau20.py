import math
def find(m,n,d):
    for i in range(m+1,n):
        for j in range(i,n):
            if(math.gcd(i,j)==d):
                print(f"{i}-{j}")

find(0,50,6)