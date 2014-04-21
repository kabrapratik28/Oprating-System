filea = open('in','r')
input = filea.read().split(" ")
userinput = 4
memory = [ ]
for kk in range(userinput):
    memory.append(-1)

nooffaults = 0 
for ss in input:
    if ss not in memory: 
        nooffaults=nooffaults+1
        memory.pop(0)
        memory.append(ss)
        print memory

print nooffaults
