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

        self.leftBar = attributesBar(self)

        self.leftBar.place(relwidth=0.25,relheight=1)


    def place_main_page_widgets(self):

        self.appTitle = CTkLabel(self,text=" - Local Digital Library (L. D. L.) -")
        self.appTitle.grid(row=1,columnspan=4)

        self.isbnEntry = CTkEntry(self,placeholder_text="Enter ISBN (13 digits)")
        self.isbnEntry.grid(row=2,columnspan=4)
        


class attributesBar(CTkFrame):

    def __init__(self,parent:CTk):
        super().__init__(parent)

        self.configure(fg_color="#0e0f0f")

        tgf.create_layout(self,3,3)

        self.create_attributesBar_widgets()


    def create_attributesBar_widgets(self):

        self.addBookButton = CTkButton(self,text="Add a Book",width=100)

        self.addBookButton.pack(side=BOTTOM,pady=5)
        
