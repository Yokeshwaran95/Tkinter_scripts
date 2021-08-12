from tkinter import *
import os

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.start_exe()
        self.end_exe()

    def start_exe(self):
        self._button = Button(self, text = "Start", command = self._openFile)
        self._button.grid()
    def end_exe(self):
        self._button = Button(self, text = "End", command = self._closeFile)
        self._button.grid()    	
    def _openFile(self):
        os.startfile("C:\\software\\chromedriver.exe")
    def _closeFile(self):
    	os.system("taskkill /im chromedriver.exe")

root = Tk()
root.title("Run an Application")
root.geometry("200x85")

app = Application(root)

root.mainloop()