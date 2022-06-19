from tkinter import *
import pyshorteners
#   For font
import tkinter.font as font
from tkinter import messagebox

root = Tk()
#   Window configurations
root.title("Url Shortener")
root.geometry('400x350')
root.configure(background="#0e1724")

#   Resize to other screen size set to false
root.resizable(False, False)

#   Shorten url when button pressed using pyshorteners module
def shortenUrl():
    #   Delete final url label
    finalUrl.config(text = "")              #   Delete existing text in label
    
    #   Accesing original url through entry
    urlName = originalUrl.get()

    #   Exception Handling
    try:
        #   Pyshorteners Mechanism to shorten urls
        s = pyshorteners.Shortener()
        shortUrl = s.tinyurl.short(urlName)
        
        #   Display shortened link to textbox   
        finalUrl.configure(text=shortUrl)
        print(shortUrl)

    except Exception as e:
        messagebox.showerror("Url Shortener", e)
    
#   Reset or clear previous activity
def reset():
    originalUrl.delete(0, "end")    #   Delete existing entry
    finalUrl.config(text = "Your short url appears here.")      #   Delete existing text in label
    
def copySuccess():
    messagebox.showinfo("Copy Success", "Copied Successfully!!")    #   Show success message box
    clip = Tk()                                                     #   Create small window
    clip.withdraw()                                                 #   Withdraw value
    clip.clipboard_clear()                                          #   Clear clipboard in Tk clipboard
    clip.clipboard_append(finalUrl.cget("text"))                    #   Get value from label and get shortened url copied to clipboard
    clip.destroy()                                                  #   Destroy this and all descendent widgets
    
    #   Now you can paste it anywhere


#   Return font attributes to apply
def getFont(fontName='Helvetica', fontSize=14, fontWeight='normal'):    #   Function with default arguments
    myFont = font.Font(family=fontName, size=fontSize, weight=fontWeight)
    return myFont

#   Make label and display in screen
headerLabel = Label(root,width=18, text = "Url Shortener", pady =10, padx = 40, bg = "#2e3856")
headerLabel['font'] = getFont('Helvetica', 24, "bold")
headerLabel.grid(row = 0, column = 0)

#   Make text box to paste link to be shortened
originalUrl = Entry(root, width=30)
originalUrl['font']= getFont("Helvetica", 16, "normal")
originalUrl.place(x = 20, y =90)

#   Make reset button
resetButton = Button(root, text = "Reset", command = reset)
resetButton['font'] = getFont("Helvetica", 12, "normal")
resetButton.place(x = 20, y = 130)

#   Make shorten button
shortenButton = Button(root, text = "Shorten", command = shortenUrl)
shortenButton['font'] = getFont("Helvetica", 12, "normal")
shortenButton.place(x = 315, y = 130)

#   Display shortened url

finalUrl = Label(root, text = "Your short url appears here.", fg = "white", bg = "#0e0e0d", width = 37, height = 2)
finalUrl['font'] = getFont('Helvetica', 14, "normal")
finalUrl.place(x = 0, y = 200)


#   Copy Button
copyButton = Button(root, text = "Click to copy", command = copySuccess)
copyButton['font'] = getFont("Helvetica", 12, "normal")
copyButton.place(x = 170, y =280)

root.mainloop()



