from customtkinter import *
import tkinterGuiFunctions as tgf


class MainPage(CTk):

    def __init__(self,widht:int=1920,height:int=1080,title:str="Test",resizable:bool=True):
        super().__init__()

        self.title(title)

        self.geometry(f"{widht}x{height}")

        self.resizable(resizable,resizable)
        
        self.create_main_page()


        self.mainloop()


    def create_main_page(self):

        tgf.create_layout(self,4,4)

        self.leftBar = libraryPanel(self,0.35,1,"#0e0d0d")

        self.topBar = ToolBar(self,1,0.05,"#5a4b47")

        


class libraryPanel(tgf.Frame):

    def __init__(self, parent, relwidth, relheight, fg_color,**kwargs):
        super().__init__(parent, relwidth, relheight, fg_color,**kwargs)

        self.setup()

        self.bar = bookInsertionPanel(self,relwidth=1,relheight=0.1,fg_color="transparent")

        self.bar.pack(side=BOTTOM,fill=X)


class bookInsertionPanel(tgf.Frame):

    def __init__(self, parent,relwidth, relheight, fg_color, **kwargs):
        super().__init__(parent,relwidth, relheight, fg_color, **kwargs)

        self.create_layout(1,2)

        self.create_book_insertion_panel_widgets()
        self.place_book_insertion_panel_widgets()    


    def create_book_insertion_panel_widgets(self):

        self.isbnEntry = CTkEntry(self,placeholder_text="Enter ISBN (13 digits)",width=300,)

        self.addBookButton = CTkButton(self,text="Add a Book",width=75)

        self.scanBarcodeButon = CTkButton(self,text="Scan Book",width=75)

    def place_book_insertion_panel_widgets(self):

        self.isbnEntry.pack(side=LEFT,fill=X,expand=True)

        self.addBookButton.pack(side=LEFT,fill=X,expand=True)

        self.scanBarcodeButon.pack(side=LEFT,fill=X,expand=True)

class ToolBar(tgf.Frame):

    def __init__(self, parent, relwidth, relheight, fg_color,**kwargs):
        super().__init__(parent, relwidth, relheight, fg_color,**kwargs)

        self.setup()
