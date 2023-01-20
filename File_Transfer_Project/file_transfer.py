import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        
        # This will set the title of the GUI Window.
        self.master.title("File Transfer")
        
        # This button is used to select files from source directory.
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # The following positions the source button in the GUI using tkinter's grid().
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # This creates entry for source directory selection.
        self.source_dir = Entry(width=75)
        # The following positions the entry in the GUI using tkinter's grid(). padx and pady are the same as
        # the buttons to ensure they line up.
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # This creates a button to select distination of files from destination directory.
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # The following positions the destination button in the GUI using tkinter's grid()
        # on the next row under the source button.
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # This creates entry for destination directory selection.
        self.destination_dir = Entry(width=75)
        # The following positions the entry in the GUI using tkinter's grid(). padx and pady are the same as
        # the buttons to ensure they line up.
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # This creates a button to transfer files.
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # This positions the transfer files button.
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # This creates an Exit button.
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # This positions the Exit button.
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


    # This is a function to select the source directory.
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget.
        # This allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry.
        self.source_dir.insert(0, selectSourceDir)


    # This is a function to select the destination directory.
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the Entry widget.
        # This allows the path to be inserted into the Entry widget properly.
        self.destination_dir.delete(0, END)
        # The .insert method will insert the user selection to the destination_dir Entry.
        self.destination_dir.insert(0, selectDestDir)


    # This is a function that exits the program.
    def exit_program(self):
        # root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window.
        root.destroy()


    def transferFiles(self):
        # This gets the current time.
        current_time = datetime.now()
        # This gets the time 24 hours ago.
        time_24_hrs_ago = current_time - timedelta(hours=24)

        # This gets the source and destination directories.
        source = self.source_dir.get()
        destination = self.destination_dir.get()

        # This gets a list of files in the source directory.
        source_files = os.listdir(source)

        # This checks and gets the time of each file.
        for i in source_files:
            file_path = os.path.join(source, i)
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # This compares the time to the time 24 hours ago.
            if file_time > time_24_hrs_ago:
                shutil.move(source + '/' + i, destination)
                print('Recent File ' + i + ' was successfully transferred.')
            




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
