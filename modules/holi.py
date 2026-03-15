import colorama as cl

"""
colorama
--holi
----yourFile



This Module(holi) Imports the library colorama
The Module, holi Is Created To Make Life Easy of a Programmer.
This module is created to access variables,
which have the color as value.
It's Short and Direct!


Tip : Do not use 'cl' as an alias after importing this module, it may 
occur technical conflicts,
It is Because I Used The word 'cl' as an alias after importing colorama.


Only Useful Data & Attributes are Created


Recomended To Not To Access 'claAF' & 'claAS' variables,
It's No Use For You!
"""


# AnsiFore (text color)
claAF = cl.ansi.AnsiFore()

black = claAF.BLACK
red =  claAF.RED
green = claAF.GREEN
white = claAF.WHITE
yellow = claAF.YELLOW
blue = claAF.BLUE
cyan = claAF.CYAN
magenta = claAF.MAGENTA
lblack = claAF.LIGHTBLACK_EX
lblue = claAF.LIGHTBLUE_EX
lcyan = claAF.LIGHTCYAN_EX
lgreen = claAF.LIGHTGREEN_EX
lmagenta = claAF.LIGHTMAGENTA_EX
lred = claAF.LIGHTRED_EX
lwhite = claAF.LIGHTWHITE_EX
lyellow = claAF.LIGHTYELLOW_EX
reset = claAF.RESET



#AnsiStyle
claAS = cl.ansi.AnsiStyle()

bright = claAS.BRIGHT
dim = claAS.DIM
normal  = claAS.NORMAL
resetStyle = claAS.RESET_ALL

# AnsiFore (text color) + AnsiStyle
bblack = claAF.BLACK + claAS.BRIGHT
bred =  claAF.RED + claAS.BRIGHT
bgreen = claAF.GREEN + claAS.BRIGHT
bwhite = claAF.WHITE + claAS.BRIGHT
byellow = claAF.YELLOW + claAS.BRIGHT
bblue = claAF.BLUE + claAS.BRIGHT
bcyan = claAF.CYAN + claAS.BRIGHT
bmagenta = claAF.MAGENTA + claAS.BRIGHT

# resetStyle leads To Reset The Color As well, So Does resetAll
resetAll = claAS.RESET_ALL
