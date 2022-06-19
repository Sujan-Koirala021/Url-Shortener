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
    
#   Reset or clear previous activity
def reset():
    originalUrl.delete(0, "end")    #   Delete existing entry
    finalUrl.delete(1.0, END)       #   Delete existing text in textbox
    


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

#   Make reset button

resetButton = Button(root, text = "Reset", command = reset)
resetButton['font'] = getFont("Helvetica", 12, "normal")
resetButton.grid(row = 5, column = 0, pady = 50)


#   Make shorten button

shortenButton = Button(root, text = "Shorten", command = shortenUrl)
shortenButton['font'] = getFont("Helvetica", 12, "normal")
shortenButton.grid(row = 3, column = 0, pady = 20)

#   Display shortened url

finalUrl = Text(root,width = 40, height = 5)
finalUrl.grid(row = 4, column = 0 , padx = 30)

root.mainloop()



