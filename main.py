from tkinter import *
import pyshorteners
#   For font
import tkinter.font as font


root = Tk()
#   Window configurations
root.title("Url Shortener")
root.geometry('400x300')

#   Resize to other screen size set to false
root.resizable(False, False)


def shortenUrl():
    urlName = 'https://www.youtube.com/watch?v=oBi16YJjf8w&ab_channel=Codemy.com'
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(urlName))

#   Return font attributes to apply
def getFont(fontName='Helvetica', fontSize=14, fontWeight='normal'):    #   Function with default arguments
    myFont = font.Font(family=fontName, size=fontSize, weight=fontWeight)
    return myFont

#   Make label and display in screen
myLabel = Label(root, text = "Url Shortener", pady =10, padx = 40)
myLabel['font'] = getFont('Helvetica', 24, "bold")
myLabel.grid(row = 0, column = 0)

#   Make text box to paste link to be shortened

linkTextbox = Text(root, width = 40, height = 5)
linkTextbox.grid(row =1, column = 0, padx=30)

#   Make shorten button

shortenButton = Button(root, text = "Shorten", command = shortenUrl)
shortenButton.grid(row = 3, column = 0, padx = 50, pady = 20)



# shortenUrl('https://www.youtube.com/watch?v=oBi16YJjf8w&ab_channel=Codemy.com')
root.mainloop()



