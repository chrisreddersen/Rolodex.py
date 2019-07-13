#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:12:24 2018

@author: chris
"""

import tkinter as tk

class rolodex(tk.Frame):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        
        
        self.name = tk.StringVar()
        self.name.set('')
        
        self.author = tk.StringVar()
        self.author.set('')
        
        name_label = tk.Label(self, text = 'Enter Book Title')
        name_label.grid(row = 1, column = 1)
        
        name_entry = tk.Entry(self,textvariable = self.name )
        name_entry.grid(row = 2, column = 1)
        
        author_label = tk.Label(self, text = 'Enter Author')
        author_label.grid(row = 3, column = 1)
        
        author_entry = tk.Entry(self,textvariable = self.author)
        author_entry.grid(row = 4, column = 1)
        
        save_button = tk.Button(self, text = 'Save', command = self.save_item)
        save_button.grid(row = 5, column = 1)
        
        quit_button = tk.Button(self, text = 'Quit')
        quit_button.grid(row = 5, column = 2)
        
    

if __name__ == '__main__':
    app = tk.Tk()
    frame = rolodex(app)
    frame.pack()
    app.mainloop()
    
        
        