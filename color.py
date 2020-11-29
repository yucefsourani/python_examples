#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os



COLORS={
        "black"        :"\033[30m",
        "red"          :"\033[31m",
        "green"        :"\033[32m",
        "yellow"       :"\033[33m",
        "blue"         :"\033[34m",
        "magenta"      :"\033[35m",
        "cyan"         :"\033[36m",
        "light_gray"   :"\033[37m",
        "dark_gray"    :"\033[90m",
        "light_red"    :"\033[91m",
        "light_green"  :"\033[92m",
        "light_yellow" :"\033[93m",
        "light_blue"   :"\033[94m",
        "light_magenta":"\033[95m",
        "light_cyan"   :"\033[96m",
        "white"        :"\033[97m"
        }
        
        
        
BG_COLORS={
        "black"        :"\033[40m" ,
        "red"          :"\033[41m" ,
        "green"        :"\033[42m" ,
        "yellow"       :"\033[43m" ,
        "blue"         :"\033[44m" ,
        "magenta"      :"\033[45m" ,
        "cyan"         :"\033[46m" ,
        "light_gray"   :"\033[47m" ,
        "dark_gray"    :"\033[100m",
        "light_red"    :"\033[101m",
        "light_green"  :"\033[102m",
        "light_yellow" :"\033[103m",
        "light_blue"   :"\033[104m",
        "light_magenta":"\033[105m",
        "light_cyan"   :"\033[106m",
        "white"        :"\033[107m"
        
        }

        
RESET="\033[0m"

def talwin_core(text,color=None,bg_color=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        new_text = ""
        if color != None:
            new_text+=COLORS[color]
        if bg_color != None:
            new_text+=BG_COLORS[bg_color]
        new_text+=text
        new_text+=RESET
    else:
        return text
    return new_text

def talwin(text,color=None,bg_color=None,**kw):
    if color not in COLORS.keys():
        color = None
        
    if bg_color not in BG_COLORS.keys():
        bg_color = None

    print(talwin_core(text,color,bg_color),**kw)
    

if __name__ == "__main__" :
    talwin("Enter your name : ","blue",end = "")
    name = input()
    talwin("Hello","green",end=" ")
    talwin(name,"red",end=" ")
    talwin("how are you?","green")
    
        

