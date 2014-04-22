AT = [0,2,4,6,8]
BT = [3,6,4,5,2]  
DONE = []
FT_DONE = []
BT_DONE = [ ]
TIME_NOW = 0 
for a in range(len(AT)):
    minimum_at  = min(AT)
    indexofmin = AT.index(minimum_at)
    timetaken = BT.pop(indexofmin)
    PROCESS_ARR = AT.pop(indexofmin)
    TIME_NOW = TIME_NOW +timetaken
    DONE.append(PROCESS_ARR)
    FT_DONE.append(TIME_NOW)
    BT_DONE.append(timetaken)

print DONE
print BT_DONE
print FT_DONE

TT = [] 
for dd in range(len(DONE)) :
    TT.append(FT_DONE[dd]-DONE[dd])

print TT

WT = []
for dd in range(len(DONE)) :
    WT.append(TT[dd]-BT_DONE[dd])

print WT
