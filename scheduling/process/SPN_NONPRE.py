AT = [0,2,4,6,8]
BT = [3,6,4,5,2]  
queueat = []
queuebt = [] 

done =  []
doneoftime = [] 

totaltime = 0 
for bb in BT :
    totaltime =totaltime + bb
BT[0]=BT[0]+1
currprocess = 0 
timerem = 0 

for a in range(totaltime+1):
    for kk in range(len(AT)):
        if a == AT[kk]:
            queueat.append(AT[kk])
            queuebt.append(BT[kk])

    if timerem == 0 and len(queueat)!=0:
        inde = queuebt.index(min(queuebt))
        v1 = queueat.pop(inde)
        v2 = queuebt.pop(inde)
        done.append(v1)
        doneoftime.append(a)
        timerem = v2-1
    else : 
        timerem = timerem -1 
        doneoftime[len(doneoftime)-1] = doneoftime[len(doneoftime)-1] + 1
    print a
    print done
    print doneoftime
    print queueat
    print queuebt
    print '-------'
print done
print doneoftime
