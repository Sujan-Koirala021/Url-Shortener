from tkinter import *
import pyshorteners

root = Tk()
root.title("Url Shortener")

def shortenUrl(urlName):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(urlName))

shortenUrl('https://www.youtube.com/watch?v=oBi16YJjf8w&ab_channel=Codemy.com')
root.mainloop()



