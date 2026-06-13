from customtkinter import *

def create_layout(widget:CTkFrame,r:int,c:int,rw:int=1,cw:int=1):
    
    widget.rowconfigure([*range(r)],weight=rw)
    widget.columnconfigure([*range(c)],weight=cw)

