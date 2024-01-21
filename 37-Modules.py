# module = a file containing python code. May contain functions , classes,etc.
# used with modular programming,which is separate a program into parts

#first way
import messages
messages.hello()
messages.bye()

#second way
import messages as msg #alias
msg.hello()
msg.bye()

#third way
from messages import hello,bye
from messages import * # for big program
hello()
bye()

help("modules") #-- for comprehensive listing of modules in python or python docs for help 