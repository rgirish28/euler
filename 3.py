tsc=600851475143
def if_prm(s):
    for p in range(2,s):
        if s%p==0:
            return False
        elif p==(s-1):
            return True
        else:
            continue

def primary(x,a):
    while x%a==0:
        x=x/a
    
    return x
z=2
while(z<tsc):
    if if_prm(z) and z<tsc:
        tsc=primary(tsc,z)
    #print tsc,' ',z
    elif z>=tsc:
        break
    z+=1

print z
