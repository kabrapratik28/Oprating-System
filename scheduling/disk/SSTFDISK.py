input = [10,4,34,10,7,19,73,2,15,6,20]
lenght = len(input)
now = 50
total = 0 
for kk in range(len(input)) :
    finaldis = 1000
    eleno = 100
    for ss in range(len(input)) :
        curr = now - input[ss]
        if curr < 0 :
            curr = curr*-1
        if curr< finaldis : 
            finaldis = curr
            eleno = ss
    kk = input[eleno]
    #print kk
    input.pop(eleno)
    curradd = now - kk
    if curradd <0 :
        curradd = curradd * -1
    total = total + curradd
    now  = kk 

print total 
print total*1.0/lenght
