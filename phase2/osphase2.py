import re
import random 
class PCB:        #PCB block  intilize by obj = PCB(10,11) ##access by obj.TTL
    TTL = 0 
    TLL = 0 
    def __init__(self,TTL,TLL):
        self.TTL = TTL 
        self.TLL = TLL


def allocate():
    global arrayofused
    while(1):
        numberall = random.randint(0,29)
        if numberall not in arrayofused  :
            arrayofused.append(numberall)
            break 
    return numberall*10

def intilization():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global arrayofused
    global PTR
    global TERMINATE_NO 
    IC = 0 
    IR =  [ '' , '' ]   ## ['GD','20'] 
    #  MEMORY INTIALIZATION *** IMPROVE HERE
    M = []
    for count in range(300):
        M.append(['','','',''])
    R = ['','','',''] 
    C = 0      ##  0 : false 1 :true
    FLAG_REGISTER = [0,3,0,0,0,0]   ## FLAG = [PI , SI , TI , EM , TTC , LLC ]
    arrayofused = []    ## used blocks array
    PTR = allocate()     ## random bolck as page table
    TERMINATE_NO = [] 
    fill_memory([0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1] , PTR)    ##page table filling

def MOS():
    ##SI = 3                                                                                            ??????? 
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    if FLAG_REGISTER[1] == 1 :
        read()
    elif FLAG_REGISTER[1] == 2:
        write()
    elif FLAG_REGISTER[1] == 3 :
        terminate()

def read():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    address_of_store = IR[1]
    final_address = int(address_of_store[0] + '0')
    #char_data =   DATACARD[:40]                           
    
    counterlenght = 0                            
    tempstr = ''
    while(counterlenght<40):
         if DATACARD[0]=="\n" :                        ## if \n is in lenght 40 then take only that
             DATACARD =DATACARD[1:] 
             break 
         tempstr= tempstr + DATACARD[0]
         DATACARD = DATACARD[1:]
         counterlenght = counterlenght + 1 
    #print tempstr
    #print M
    char_data = tempstr
    listofchar = spilt_str(char_data)
    fill_memory(listofchar , final_address )                     ##  ???????????????????????????????????????????????????????? ***OUT of DATA
    #DATACARD =  DATACARD[40:]                     

def write():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    address_of_store = IR[1]
    final_address = int(address_of_store[0] + '0')
    counter_of_mem = 0 
    while (counter_of_mem<=9): 
        li_chrs = read_memory(final_address )
        OUT = OUT + mergestring(li_chrs)                               
        final_address = final_address + 1
        counter_of_mem = counter_of_mem +1                          ## ********************************* TLL check ?? 
    write_to_file()
def terminate():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR                                                       ## *********************************88 normal or abnormal exexcution
    OUT = OUT + '\n\n'
    write_to_file()
    load()

def load():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    global obj_TTL_TLL
    intilization()
    card = ''
    OUT= ''
    eof = 1
    for line in input_file:
        eof = 0 
	if (re.search(r'^\$END(\d)+',line)):              
		break 
	else :
		card = card + line                                                ##  line[:40].strip("\n\r\t")
    if eof :
        #End Of Program
        print "Done !!!"
        exit()
    if "$AMJ" in card :
        list_card_data = split_data_program(card)
        INSTRUC = list_card_data[0]
        DATACARD = list_card_data[1]
        numbers_in_AMJ = list_card_data[2]
        obj_TTL_TLL = PCB(int(numbers_in_AMJ[4:8]),int(numbers_in_AMJ[8:]))
        listofchar = spilt_str(INSTRUC)  ##instructions character
        ## fill in memory here
        ##fill_memory(listofchar , 0, 0 )   ## list , row and col
        lenghtofinstru = len(listofchar)
        pagebaseaddress = PTR
        while(lenghtofinstru>0):                ## program card storing at random places and entry saving in page table
            randomblockno = allocate()
            fill_memory(listofchar[:40],randomblockno)
            basenumber = '0000'+ str(randomblockno/10)   ## adding safeside '0000' bz if basenumber is just 1 how to fill in 4 memory 
            basechars = spilt_str(basenumber)  ##'000001' = >  ['0','0','0','0','0','1']
            baselistofchar = spilt_str(basechars[len(basechars)-3:])    ##last 3 digit only
            totalpasstomemory = [1,] + map(int,baselistofchar)
            fill_memory(totalpasstomemory,pagebaseaddress)
            listofchar=listofchar[40:]
            lenghtofinstru = len(listofchar)
            pagebaseaddress = pagebaseaddress+1 
    else :
        print "JOB CARD NOT CONTAIN $AMJ OR DONT GIVE ENTER AFTER LAST $END"
        exit()
def startexecution():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR

    IC = 0
    executeuserprogram()
    
def executeuserprogram():
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    while True : 
        RA_IC = address_map(IC)
        #print RA_IC
        li_chrt = read_memory(RA_IC)
        str_oper = mergestring(li_chrt)
        IR[0] = str_oper[:2]
        IR[1] = str_oper[2:]
        IC = IC + 1
        if IR[0]=="LR" : 
            R = read_memory(int (IR[1]) )
        elif IR[0]=="SR" :
            tempR = R [:]                                            ## ******************************** copy this way
            fill_memory(tempR , int(IR[1]))
        elif IR[0]=="CR" :
            #print R
            #print read_memory(int (IR[1]) )
            if R == read_memory(int (IR[1]) ):
                C = 1 
            else: 
                C = 0 
        elif IR[0]=="BT" :
            if C== 1: 
                IC = int (IR[1])
        elif IR[0]=="GD" :
            FLAG_REGISTER[1] = 1 
            MOS()
        elif IR[0]=="PD" :
            FLAG_REGISTER[1] = 2
            MOS()
        elif IR[0]=="XX" : 
            None 
        elif IR[0]=="H" :            ##** See String 
            FLAG_REGISTER[1] = 3
            MOS()
            break 
        else : 
            print "Wrong Operand"
            print "IR : "+ str(IR)
            #exit()
        
## ['G','D'] => 'GD'
def mergestring(list_char):
    stri_made = ''
    for chars in list_char : 
        stri_made  = stri_made + str(chars)
    return stri_made 


## 'GD' => ['G','D']
def spilt_str(stri):
    lis_ret = [ ]
    for e in stri :
        lis_ret.append(e)
    return lis_ret


def fill_memory(listofchar , row, col=0 ):
 
    global IC
    global IR
    global M
    global C
    global FLAG_REGISTER
    #global R 
    global DATACARD
    global OUT
    global input_file
    global eof
    global PTR
    lenlist = len(listofchar)
    hori = row 
    ver = col 
    innerloop = 0
    ##FIRST CLEAR GARBAGE BEFORE SORING NEW BLOCK OF DATA AT THAT BLOCK**************************
    
    counter_for_garbage = 0 
    colcounter = 0 
    while(counter_for_garbage<10):
        while(colcounter<4):
            M[hori][colcounter] = ''
            colcounter = colcounter + 1
        counter_for_garbage = counter_for_garbage + 1 
        colcounter = 0 

    while(hori < 300):
        while(col < 4):
            if lenlist > 0:
                M[hori][col] = listofchar.pop(0)
                lenlist = lenlist -1
                col = col + 1
            elif lenlist==0 :
                innerloop =1 
                break 
        col = 0 
        hori = hori + 1 
        if innerloop : 
            break 
    
    if (lenlist > 0 ):
        print "WRITE MEMORY OUT OF BOUND ERROR . "
        exit()


def read_memory( row , col = 0 ):

    global M 
    li_char = []
    if (row > 299 or row < 0 or col>3 or col <0):
        #print "PTR :"+ str(PTR)
        print "READ MEMORY OUT OF BOUND ERROR . "
        exit()
        
    while (col < 4):
        li_char.append(M[row][col])
        col = col + 1 

    return li_char




def  write_to_file():

    global OUT 

    opentowrite = open('out','a')
    OUT = OUT.strip("\00")
    if '\n' not  in OUT : 
        OUT = OUT + "\n"
    opentowrite.write(str(OUT)) 
    opentowrite.close()
    OUT = ''           ## BUffer written to file and so now empty 


def split_data_program(card):
    pcard =  "pcard"
    dcard = "dcard"
    pcardstr = ""
    dcardstr = ""
    temp = pcard 
    array_of_line = card.split("\n")
    allnumberrelated = "000000000000"
    for everyline in array_of_line :
        if (re.search(r'^\$AMJ(\d)+',everyline)):
            temp = pcard 
            allnumberrelated = everyline[4:]    ## 3 numbers 
        elif (re.search(r'^\$DTA',everyline)):
            temp = dcard
        elif temp=="pcard" : 
            everyline = everyline.strip("\n\r\t ")
            pcardstr = pcardstr + everyline[:40]
        elif temp=="dcard"  :
            everyline = everyline.strip("\r")
            everyline = everyline + "\n"
            dcardstr = dcardstr + everyline[:40]
    return [pcardstr,dcardstr,allnumberrelated]


def address_map(VA):    ## int VA
    global FLAG_REGISTER 
    global PTR
    global M
    if (str(VA)<'0' or str(VA)>'99' or (not str(VA).isdigit())):
        #print VA
        FLAG_REGISTER[0]=2   ## FLAG = [PI , SI , TI , EM , TTC , LLC ]
        return -1
    else :
        base  = VA/10 
        displaced_add = PTR + base
        if (M[displaced_add][0]==0):
            FLAG_REGISTER[0]= 3
            return -1 
        else :
            stringofRAbase = mergestring([str(M[displaced_add][1]),str(M[displaced_add][2]),str(M[displaced_add][3])])
            intofRAbase = int(stringofRAbase)
            RA = intofRAbase*10 + VA % 10 
            return RA


def simulation(): 
    global FLAG_REGISTER     ## FLAG = [PI , SI , TI , EM , TTC , LLC ]
    global obj_TTL_TLL  
    FLAG_REGISTER[4] = FLAG_REGISTER[4] +1 
    if (FLAG_REGISTER[4]==obj_TTL_TLL.TTL):
        FLAG_REGISTER[2] = 2


input_file = open('in','r')
load()
print "PTR ------ >> " + str(PTR)
for cc in M:
	print cc

while True :
   startexecution()
    

