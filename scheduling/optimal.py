filea = open('in','r')
input = filea.read().split(" ")
userinput = 4
memory = []
usedtime = [] 
pagefault = 0 
for kk in range(userinput):
    memory.append(-1)
    usedtime.append(100)

for ss in range(len(input)):
    if input[ss] not in memory :
        pagefault = pagefault + 1
        searchfrom = ss+1
        for uu in range(len(usedtime)):
            usedtime[uu] = 0 
        for ads in range(len(memory)) :
            for tty in input[searchfrom:]:
                if tty==memory[ads]:
                    break
                else :
                    usedtime[ads]= usedtime[ads] +1
        dd= usedtime.index(max(usedtime))
        memory[dd]=input[ss]
        usedtime[dd]=0 
    else :
        "No page fault"

print pagefault
