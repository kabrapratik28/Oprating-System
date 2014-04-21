input = [10,4,34,10,7,19,73,2,15,6,20]
lenght = len(input)
now = 50
total = 0 

input.sort()
mark = 0 
for aa in range(len(input)) : 
    if now > input[aa] :
        None
        mark = aa
    else : 
        curradd = input[aa]-now
        if curradd<0: 
            curradd = curradd*-1
        total = total + curradd
        now = input[aa]
total = total + input[len(input)-1] - input[0]
now = input[0]

for aa in range(1,mark+1):
    curr = input[aa]-now
    if curr < 0 :
        curr = curr * -1
    total  = total + curr
    now = input[aa] 

print total 
print total*1.0/len(input)
