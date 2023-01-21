import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.customPage = StringVar()

        self.lblCustom = Label(self.master,text='Enter custom text or click the Default HTML page button', font=('Helvetica', 16))
        self.lblCustom.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.txtCustom = Entry(self.master,text=self.customPage, font=('Helvetica', 16))
        self.txtCustom.grid(row=1, column=0, columnspan=10, padx=(30,0), pady=(30,0), sticky=W)

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2)

        self.btn2 = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.customHTML)
        self.btn2.grid(row=2, column=3)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        htmlText = self.customPage.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
