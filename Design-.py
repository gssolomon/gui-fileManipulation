# -*- coding: utf-8 -*-

#Created on Mon Dec 11 16:18:45 2017

#@author: glenn


import tkinter as tk
from PIL import Image, ImageTk

class Design:
    
    def __init__(self, top):
        
        #Label to Enter first name
        self.fn=tk.Label(top, text = "Enter your First Name:")
        self.fn.grid(row = 2, column = 1, sticky = tk.E, padx=20, pady=20)
        
        #Entrybox for first name
        self.fnen=tk.Entry(top)
        self.fnen.grid(row = 2, column = 2, padx=20, pady=20)
        
        #Label to Enter last name
        self.ln=tk.Label(top, text = "Enter your Last Name:")
        self.ln.grid(row = 3,  column = 1, sticky = tk.E, padx=20, pady=20)
        
        #Entrybox for last name
        self.lnen=tk.Entry(top)
        self.lnen.grid(row = 3, column = 2, padx=20, pady=20)
        
        #Button to conduct operation and calling the onClick() command through callback
        self.add = tk.Button(top, text = "Add Me", command = lambda: self.onClick())
        self.add.grid(row=4, column=1, columnspan=3)
        
        #Inserting image via ImageTK
        self.image = Image.open("Mario.gif")
        self.photo1 = ImageTk.PhotoImage(self.image)
        self.label_photo1 = tk.Label(top, image=self.photo1)
        self.label_photo1.grid(row=0,column=0,rowspan=2)
        
        self.photo2 = ImageTk.PhotoImage(self.image)
        self.label_photo2 = tk.Label(top, image=self.photo2)
        self.label_photo2.grid(row=0,column=3,rowspan=2)
        
        self.photo3 = ImageTk.PhotoImage(self.image)
        self.label_photo3 = tk.Label(top, image=self.photo3)
        self.label_photo3.grid(row=5,column=0,rowspan=2)
        
        self.photo4 = ImageTk.PhotoImage(self.image)
        self.label_photo4 = tk.Label(top, image=self.photo4)
        self.label_photo4.grid(row=5,column=3,rowspan=2)
        
    def onClick(self):
        
        #Retrieving texts entered in entrybox 1 and 2
        self.st1 = self.fnen.get()
        self.st2 = self.lnen.get()
        
        self.names = []
        
        #Reading the WithoutMe file and adding the first and last name and then sorting the names via last name
        with open('WithoutMe.txt', 'r') as f1:
            self.names = [line.strip() for line in f1]
            self.names.append(self.st2 + ', ' + self.st1)
            self.names.sort()
            self.names = [x for x in self.names if x != '']
            print(self.names)
            f1.close()
            
        #Creating the WithMe file if not exists and adding the sorted names in it
        with open('WithMe.txt', 'w') as self.f2:
            self.printNames = ""
            for x in self.names:
                self.printNames = self.printNames + x + '\n'
            self.f2.write(self.printNames)
            
        
        #Displaying the sorted name in the GUI
        self.listing = tk.Label(root, text = self.printNames)
        self.listing.grid(row = 2, column = 1, columnspan=3, rowspan = 2, sticky = tk.W + tk.E)           
        
        #Destroying the addme button
        self.add.destroy()
        
        #To exit from the gui
        self.exit_button = tk.Button(root, text = "Exit", command = self.exit_case)#.grid(row = 4, column = 1, columnspan = 3, padx = 7, pady = 7)
        self.exit_button.grid(row = 9, column = 1, columnspan = 3, padx = 7, pady = 7)
        
        #self.fn.grid_forget()
        self.fnen.destroy()
        #self.ln.grid_forget()
        self.lnen.destroy()
        
        
        
        self.new_widget = tk.Label(root, text = "EXIT PAGE")
        self.new_widget.grid(row = 7, column = 1, columnspan=2, rowspan = 2, sticky = tk.W + tk.E)
        
        self.label_photo1.destroy()
        self.label_photo2.destroy()
        self.label_photo3.destroy()
        self.label_photo4.destroy()
        
        
        self.image=self.image.resize((64,64),Image.ANTIALIAS)
        #ANTIALIAS is for high-quality downsampling/resizing
        
        self.photo5 = ImageTk.PhotoImage(self.image)
        label_photo5 = tk.Label(root, image=self.photo5)
        label_photo5.grid(row=0,column=0,rowspan=2)
        

        self.photo6 = ImageTk.PhotoImage(self.image)
        label_photo6 = tk.Label(root, image=self.photo6)
        label_photo6.grid(row=0,column=5,rowspan=2)
        
    
        self.photo7 = ImageTk.PhotoImage(self.image)
        label_photo7 = tk.Label(root, image=self.photo7)
        label_photo7.grid(row=10,column=0,rowspan=2)
        
       
        self.photo8 = ImageTk.PhotoImage(self.image)
        label_photo8 = tk.Label(root, image=self.photo8)
        label_photo8.grid(row=10,column=5,rowspan=2)
        
        
    #To sort names according to last name
    def getKey(self, item):
        return item[0]
        
    #On clicking the exit button     
    def exit_case(self):
        
        root.destroy()
        

root=tk.Tk()
app=Design(root)
root.mainloop()
