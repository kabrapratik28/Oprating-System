filea = open('in','r')
input = filea.read().split(" ")
userinput = 3
memory = []
usedtime = [] 
pagefault = 0 
for kk in range(userinput):
    memory.append(-1)
    usedtime.append(100)

for ss in input : 
    if ss in memory : 
        valu = memory.index(ss)
        for aaa in range(len(usedtime)):
            usedtime[aaa]=usedtime[aaa]+1
        usedtime[valu]=0 
    else :
        throw = usedtime.index(max(usedtime))
        for aaa in range(len(usedtime)):
            usedtime[aaa]=usedtime[aaa]+1
        memory[throw] = ss
        usedtime[throw]=0 
        pagefault = pagefault +1 

print pagefault
