
# Url Shortener

This is a simple GUI app made using Tkinter that makes urls short using the most famous URL Shorteners availables.

The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.

## Demo

![20220619_182417](https://user-images.githubusercontent.com/84112374/174481374-bc1c7498-d868-4b25-b370-f84b42b289b0.gif)

## Installation

```bash
pip install pyshorteners

```

## Documentation
- [Tkinter](https://docs.python.org/3/library/tk.html)
- [Pyshorteners](https://pyshorteners.readthedocs.io/en/latest/)



## FAQ

#### How do I make urls short?
Well, it is very easy as typing to generate the short url.
```bash
import pyshorteners

s = pyshorteners.Shortener()
print(s.tinyurl.short('http://www.g1.com.br'))
```
    
## Authors

 [@Sujan_Koirala](https://github.com/Sujan-Koirala021)
