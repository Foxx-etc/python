"""Only visualizing the colors of Traffic Light and not text with colors"""

import time
import colorama as c

bgcolor = c.ansi.AnsiBack()
textcolor = c.ansi.AnsiFore()



# traffic_light_name : [seconds, background_color, text_color]
traff_light= {
    "RED":[2, bgcolor.RED, textcolor.RED],
    "YELLOW":[1, bgcolor.YELLOW, textcolor.YELLOW],
    "GREEN":[2, bgcolor.GREEN, textcolor.GREEN]
}


while True:
    for v,k in zip(traff_light.values(), traff_light.keys()):
        time.sleep(v[0])
        print(v[1], v[2])        # text_color
        print(k)         # .keys()


