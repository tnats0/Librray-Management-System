from customtkinter import *


class Frame(CTkFrame):

    def __init__(self,parent,relwidth:float,relheight:float,fg_color:str,**kwargs):
        super().__init__(master=parent,fg_color=fg_color,**kwargs)

        self.relwidth = relwidth
        self.relheight = relheight


    def setup(self):

        self.place(relwidth=self.relwidth,relheight=self.relheight)

    def create_layout(self,r:int,c:int,rw:int=1,cw:int=1):
    
        self.rowconfigure([*range(r)],weight=rw)
        self.columnconfigure([*range(c)],weight=cw)




def create_layout(widget:CTk,r:int,c:int,rw:int=1,cw:int=1):
    
        widget.rowconfigure([*range(r)],weight=rw)
        widget.columnconfigure([*range(c)],weight=cw)