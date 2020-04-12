#!/usr/bin/python
from pathlib import Path

import tkinter as tk
from tkinter import ttk

import pandas

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

class DNNWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.grid_columnconfigure(0, weight = 1)

        
