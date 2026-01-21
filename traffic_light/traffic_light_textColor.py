"""Only visualizing the colors of traffic lights in text format"""

import time
import colorama as c

textcolor = c.ansi.AnsiFore()



# traffic_light_name : [seconds, text_color]
traff_light= {
    "RED":[2, textcolor.RED],
    "YELLOW":[1, textcolor.YELLOW],
    "GREEN":[2, textcolor.GREEN]
}


while True:
    for v,k in zip(traff_light.values(), traff_light.keys()):
        time.sleep(v[0])
        print(v[1])        # text_color
        print(k)         # .keys()


