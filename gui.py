
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from run_cherry import *
from tkinter import IntVar
import os
from main_loop_logic import *

class MyFrame(Frame):



    def __init__(self):



        Frame.__init__(self)
        self.master.title("Cherry Pick Creator")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)
        self.radiovariable = IntVar()
        self.head = StringVar()
        self.head = ' '
        self.filenamestring = "before"


        self.button2 = Button(self, text="Load CSV", command=self.load_file, width=10)
        #self.radiobutton1 = Radiobutton(self, text="Replicates on Different Plates", variable=self.radiovariable, value=1, command=self.radio_sel)
        #self.radiobutton1.grid(row=1, column=0, sticky=W)
        #self.radiobutton2 = Radiobutton(self, text="Replicates on Same Plate", variable=self.radiovariable, value=2, command=self.radio_sel)
        #self.radiobutton2.grid(row=1, column=1, sticky=W)
        self.plate_reps_lbl = Label(self, text="Plate Copies")
        self.plate_reps_lbl.grid(row=0, column=0, sticky=W)
        self.plate_reps_lbl2 = Label(self, text="Replicates Per Plate")
        self.plate_reps_lbl2.grid(row=0, column=1, sticky=W)
        self.button2.grid(row=3, column=0, sticky=W)
        self.spinbox = Spinbox(self, from_=1, to=50, command=self.spin_com)
        self.spinbox.grid(row=2, column=0, sticky=W)
        self.spinbox2 = Spinbox(self, from_=1, to=50, command=self.spin_com)
        self.spinbox2.grid(row=2, column=1, sticky=W)
        self.filneame_lable = Label(self, text=self.head)
        self.filneame_lable.grid(row=3, column=1, sticky=W)
        self.gobutton = Button(self, text="Run", command=self.run_program, width=10)
        self.gobutton.grid(row=4, column=0, sticky=W)
        self.spin_com()

    def load_file(self):
        fpath = askopenfilename(filetypes=(("Csv", "*.csv"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        if fpath:
            try:
                #print("""here it comes: self.settings["template"].set(fname)""")

                filename = os.path.basename(fpath)

                self.filneame_lable.config(text=filename)
                self.filenamestring = fpath

            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fpath)



        return(fpath)

    def radio_sel(self):
        self.radiochoice = self.radiovariable.get()
        print(self.radiochoice)

    def spin_com(self):
        self.spinboxvalue = self.spinbox.get()
        self.spinbox2value = self.spinbox2.get()
        print(self.spinboxvalue)
        print(self.spinbox2value)

    def run_program(self):
        parse_gui_options(self.filenamestring, int(self.spinboxvalue), int(self.spinbox2value))




if __name__ == "__main__":
    MyFrame().mainloop()