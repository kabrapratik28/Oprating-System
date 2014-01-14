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
    
    address_of_store = IR[1]
    final_address = address_of_store[0] + '0'
    
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
    ## print two lines 
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
    card = ''
    eof = 1
    for line in input_file:
        eof = 0 
	if (line=='$END\n'):
		break 
	else :
		card = card + line
    if eof :
        #================================ End OF program ======================
        print "Done !!!"
        exit()
    splitamj = card.split("$AMJ")
    amjanddata = splitamj[1].split("$DATA\n")
    AMJCARD = amjanddata[0].strip('\n')
    DATACARD  = amjanddata[1].strip('\n')
    INSTRUC = AMJCARD[13:]
    
    listofchar = spilt_str(INSTRUC)
    ## fill in memory here
    

def startexecution():
    global IC
    global IR
    global M
    global C
    global SI
    IC = 0 
    executeuserprogram()

def executeuserprogram():
    '''
    loop 
       IR = M[IC]
       IC = IC +1 
       EXAMINE IR [1,2]
                LR:	R ← M [IR[3,4]]
		SR:	R → M [IR[3,4]]
		CR: 	Compare R and M [IR[3,4]]
			If equal C ← T else C ← F	
		BT:	If C = T then IC ← IR [3,4]
		GD:	SI = 1
		PD: 	SI = 2
		H:	SI = 3
      END examine
    END LOOP  '''
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
        print "OVERFLOW !!! MEMORY OUT OF BOUND ERROR . "
        exit()
