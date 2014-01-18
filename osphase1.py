'''
IC= instruction counter
IR= instruction register
Memory = 100*4  ## bolcks of 10
R= General purpose Register
SI= system interupt
in = Input file ... JOB card
out = Output file 
'''
import re 
def intilization():
    '''
    IC = 0 
    IR = 0 
    Memory = 0 
    R = 0  # general pupose register 
    SI = 3 # system interupt 
    '''
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    IC = 0 
    IR =  [ '' , '' ]   ## ['GD','20'] 
    #  MEMORY INTIALIZATION *** IMPROVE HERE
    M = []
    for count in range(100):
        M.append(['','','',''])
    R = ['','','',''] 
    C = 0      ##  0 : false 1 :true
    SI = 3
    

def MOS():
    '''
    #master mode
    SI = 3
    case 
    1 read
    2 write
    3 terminate
    endcase
    '''
    ##SI = 3                                                                                            ??????? 
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    if SI == 1 :
        read()
    elif SI == 2:
        write()
    elif SI == 3 :
        terminate()

def read():
    '''
    IR[4] = 0 
    read(in) upto 10 bytes IR[3,4] to  IR[3,4] + 9   ## read one block whole
               **** # while reading M[IR[3,4]] = $END (abort program)
    executeprogram   (return control to excute program)
    '''
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    address_of_store = IR[1]
    final_address = int(address_of_store[0] + '0')
    char_data =   DATACARD[:40]
    listofchar = spilt_str(char_data)
    fill_memory(listofchar , final_address )
    DATACARD =  DATACARD[40:]

def write():
    '''
    IR[4] = 0 
    write(out) upto 10 bytes IR[3,4] to  IR[3,4] + 9  ## write one block 
    executeprogram   (return control to excute program)
    '''
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    address_of_store = IR[1]
    final_address = int(address_of_store[0] + '0')
    counter_of_mem = 0 
    while (counter_of_mem<=9): 
        li_chrs = read_memory(final_address )
        OUT = OUT + mergestring(li_chrs)                               
        final_address = final_address + 1
        counter_of_mem = counter_of_mem +1 
    write_to_file()
def terminate():
    '''
    print two blank lines
    MOS / LOAD      ## First load the program then mos
    '''
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    OUT = OUT + '\n'
    write_to_file()
    load()

def load():
    '''
    point to memory 0  ## m <-0 
    while not e-o-f
         read next card into buffer
               control card : 
                   $AMJ , end-while
                   $DTA , MOS / start execuation
                   $END , end while
               Program card : 
                   IF M = 100 ABORT (memory exceeded)
                   store buffer in memory locations m to m+9
                   m<-m+10
         end while
         stop
    '''
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof


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
        '''                                           ## <<=========   read card ()
        splitamj = card.split("$AMJ")
        amjanddata = splitamj[1].split("$DATA\n")
        AMJCARD = amjanddata[0].strip('\n')
        DATACARD  = amjanddata[1].strip('\n')
        INSTRUC = AMJCARD[13:]
        '''
        list_card_data = split_data_program(card)
        INSTRUC = list_card_data[0]
        DATACARD = list_card_data[1]
        listofchar = spilt_str(INSTRUC)
        ## fill in memory here
        fill_memory(listofchar , 0, 0 )   ## list , row and col

    else :
        print "JOB CARD NOT CONTAIN $AMJ OR DONT GIVE ENTER AFTER LAST $END"
        exit()
def startexecution():
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof


    IC = 0
    executeuserprogram()
    
def executeuserprogram():
    global IC
    global IR
    global M
    global C
    global SI
    global R 
    global DATACARD
    global OUT
    global input_file
    global eof

    while True : 
        li_chrt = read_memory(IC)
        str_oper = mergestring(li_chrt)
        IR[0] = str_oper[:2]
        IR[1] = str_oper[2:]
        IC = IC + 1
        if IR[0]=="LR" : 
            R = read_memory(int (IR[1]) )
        elif IR[0]=="SR" :
            fill_memory(R , int(IR[1]))
        elif IR[0]=="CR" :
            if R == read_memory(int (IR[1]) ):
                C = 1 
            else: 
                C = 0 
        elif IR[0]=="BT" :
            if C== 1: 
                IC = int (IR[1])
        elif IR[0]=="GD" :
            SI = 1 
            MOS()
        elif IR[0]=="PD" :
            SI = 2
            MOS()
        elif IR[0]=="XX" : 
            None 
        elif IR[0]=="H" :            ##** See String 
            SI = 3
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
        stri_made  = stri_made + chars
    return stri_made 


## 'GD' => ['G','D']
def spilt_str(stri):
    lis_ret = [ ]
    for e in stri :
        lis_ret.append(e)
    return lis_ret


def fill_memory(listofchar , row, col=0 ):
 
    global M

    lenlist = len(listofchar)
    hori = row 
    ver = col 
    innerloop = 0

    while(hori < 100):
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
    if (row > 99 or row < 0 or col>3 or col <0):
        print "READ MEMORY OUT OF BOUND ERROR . "
        exit()
        
    while (col < 4):
        li_char.append(M[row][col])
        col = col + 1 

    return li_char




def  write_to_file():

    global OUT 

    opentowrite = open('out','a')
    opentowrite.write(str(OUT)+"\n") 
    opentowrite.close()
    OUT = ''           ## BUffer written to file and so now empty 


def split_data_program(card):
    pcard =  "pcard"
    dcard = "dcard"
    pcardstr = ""
    dcardstr = ""
    temp = pcard 
    array_of_line = card.split("\n")
    for everyline in array_of_line :
        if (re.search(r'^\$AMJ(\d)+',everyline)):
            temp = pcard 
        elif (re.search(r'^\$DTA',everyline)):
            temp = dcard
        elif temp=="pcard" : 
            everyline = everyline.strip("\n\r\t ")
            pcardstr = pcardstr + everyline[:40]
        elif temp=="dcard"  :
            everyline = everyline.strip("\n\r\t ")
            dcardstr = dcardstr + everyline[:40]
    return [pcardstr,dcardstr]

input_file = open('in','r')
load()
while True :
    startexecution()
    
