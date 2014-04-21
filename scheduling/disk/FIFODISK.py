input = [10,4,34,10,7,19,73,2,15,6,20]
now = 50
total = 0 
for kk in input :
    curradd = now - kk
    if curradd <0 :
        curradd = curradd * -1
    total = total + curradd
    now  = kk

print total 
print total*1.0/len(input)
