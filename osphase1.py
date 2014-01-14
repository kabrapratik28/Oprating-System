input_file = open('in','r')


'''
IC= instruction counter
IR= instruction register
Memory = 100*4  ## bolcks of 10
R= General purpose Register
SI= system interupt
in = Input file ... JOB card
out = Output file 
'''
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
    IC = 0 
    IR =  [ '' , '' ]   ## ['GD','20'] 
    #  MEMORY INTIALIZATION *** IMPROVE HERE
    M = []
    for count in range(100):
        M.append(['','','',''])
    R = 0 
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

    if SI == 1 :
        read()
    elif SI == 2:
        write()
    else :
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
    global DATACARD
    address_of_store = IR[1]
    final_address = int(address_of_store[0] + '0')
    char_data =   DATACARD[:40]
    listofchar = spilt_str(char_data)
    fill_memory(listofchar , final_address ):
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
    global OUT
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
    global OUT
    OUT = OUT + '\n\n'
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
    global input_file
    global eof 
    global DATACARD
    global OUT
    intilization()
    card = ''
    OUT= ''
    eof = 1
    for line in input_file:
        eof = 0 
	if (line=='$END\n'):
		break 
	else :
		card = card + line
    if eof :
        #End Of Program
        print "Done !!!"
        exit()
    splitamj = card.split("$AMJ")
    amjanddata = splitamj[1].split("$DATA\n")
    AMJCARD = amjanddata[0].strip('\n')
    DATACARD  = amjanddata[1].strip('\n')
    INSTRUC = AMJCARD[13:]
    
    listofchar = spilt_str(INSTRUC)
    ## fill in memory here
    fill_memory(listofchar , 0, 0 )   ## list , row and col

def startexecution():
    global IC
    global IR
    global M
    global C
    global SI
    IC = 0 
    executeuserprogram()

def executeuserprogram():
    global IC
    global IR
    global M
    global C
    global SI
    




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
    lenlist = len(listofchar)
    hori = row 
    ver = col 
    innerloop = 0
 
    global M

    while(hori < 100):
        while(col < 4): 
            M[hori][col] = listofchar.pop(0)
            lenlist = lenlist -1
            col = col + 1
            if lenlist==0 :
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
    li_char = []
    global M
    if (row > 99 or row < 0 or col>3 or col <0):
        print "READ MEMORY OUT OF BOUND ERROR . "
        exit()
        
    while (col < 4):
        li_char.append(M[row][col])
        col = col + 1 

    return li_char




def  write_to_file():
    global OUT 
    opentowrite = open('out','w')
    opentowrite.write(OUT)
    opentowrite.close()
    OUT = ''           ## BUffer written to file and so now empty 
