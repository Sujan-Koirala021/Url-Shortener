from tkinter import *
import pyshorteners
#   For font
import tkinter.font as font


root = Tk()
#   Window configurations
root.title("Url Shortener")
root.geometry('400x350')

#   Resize to other screen size set to false
root.resizable(False, False)

#   Shorten url when button pressed using pyshorteners module
def shortenUrl():
    #   Delete final url textbox
    finalUrl.delete(1.0, END)
    
    #   Accesing original url through entry
    urlName = originalUrl.get()

    #   Pyshorteners Mechanism to shorten urls
    s = pyshorteners.Shortener()
    shortUrl = s.tinyurl.short(urlName)
    
    #   Display shortened link to textbox   
    finalUrl.insert(END, shortUrl)
    

#   Return font attributes to apply
def getFont(fontName='Helvetica', fontSize=14, fontWeight='normal'):    #   Function with default arguments
    myFont = font.Font(family=fontName, size=fontSize, weight=fontWeight)
    return myFont

#   Make label and display in screen
headerLabel = Label(root, text = "Url Shortener", pady =10, padx = 40)
headerLabel['font'] = getFont('Helvetica', 24, "bold")
headerLabel.grid(row = 0, column = 0)

#   Make text box to paste link to be shortened

originalUrl = Entry(root, width=30)
originalUrl['font']= getFont("Helvetica", 16, "normal")
originalUrl.grid(row =1, column = 0, padx=5)

#   Make shorten button

shortenButton = Button(root, text = "Shorten Link", command = shortenUrl)
shortenButton['font'] = getFont("Helvetica", 12, "normal")
shortenButton.grid(row = 3, column = 0, padx = 50, pady = 20)

#   Display shortened url

finalUrl = Text(root,width = 40, height = 5)
finalUrl.grid(row = 4, column = 0 , padx = 30)

root.mainloop()



