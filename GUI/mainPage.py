from customtkinter import *


class MainPage:

    def __init__(self,widht:int=500,height:int=500,title:str="Test",resizable:bool=True):
        
        self.widht = widht
        self.height = height
        self.title = title
        self.resizable = resizable

        self.mainPage = self.create_main_page()

        self.create_main_page_layout()
        self.place_main_page_widgets()

        self.mainPage.mainloop()


    def create_main_page(self):

        self.newMainPage = CTk()

        self.newMainPage.title(self.title)

        self.newMainPage.geometry(f"{self.widht}x{self.height}")

        self.newMainPage.resizable(self.resizable,self.resizable)

        return self.newMainPage
    
    def create_main_page_layout(self):

        self.mainPage.rowconfigure([*range(4)],weight=1)
        self.mainPage.columnconfigure([*range(4)],weight=1)

    def place_main_page_widgets(self):

        self.appTitle = CTkLabel(self.mainPage,text=" - Local Digital Library (L.D.L.) -")
        self.appTitle.grid(row=1,columnspan=4)

        self.isbnEntry = CTkEntry(self.mainPage)
        self.isbnEntry.grid(row=2,columnspan=4)
        


