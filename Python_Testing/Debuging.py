#debuging
#linting
#ide/editor
#read error
''' 
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

'''
import pdb


def addNum(num1, num2):
    pdb.set_trace()
    t = 10 * 30
    return num1 + num2


print(addNum(10, "2ee2"))
