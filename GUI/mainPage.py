from customtkinter import *
import tkinterGuiFunctions as tgf


class MainPage(CTk):

    def __init__(self,widht:int=500,height:int=500,title:str="Test",resizable:bool=True):
        super().__init__()

        self.title(title)

        self.geometry(f"{widht}x{height}")

        self.resizable(resizable,resizable)
        
        self.create_main_page()


        self.mainloop()


    def create_main_page(self):

        tgf.create_layout(self,4,4)

        self.place_main_page_widgets()

        self.leftBar = attributesBar(self,0.35,1,"#0e0d0d")

        self.topBar = TopBar(self,1,0.05,"#5a4b47")



    def place_main_page_widgets(self):

        self.appTitle = CTkLabel(self,text=" - Local Digital Library (L. D. L.) -")
        self.appTitle.grid(row=1,columnspan=4)

        


class attributesBar(tgf.Frame):

    def __init__(self, parent, relwidth, relheight, fg_color,**kwargs):
        super().__init__(parent, relwidth, relheight, fg_color,**kwargs)

        self.setup()

        self.create_layout(3,3)

        self.create_attributesBar_widgets()


    def create_attributesBar_widgets(self):

        self.addBookButton = CTkButton(self,text="Add a Book",width=100)
        self.addBookButton.pack(side=BOTTOM)

        self.isbnEntry = CTkEntry(self,placeholder_text="Enter ISBN (13 digits)")
        self.isbnEntry.pack(side=BOTTOM)


class TopBar(tgf.Frame):

    def __init__(self, parent, relwidth, relheight, fg_color,**kwargs):
        super().__init__(parent, relwidth, relheight, fg_color,**kwargs)

        self.setup()
