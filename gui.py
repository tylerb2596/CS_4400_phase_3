#CS 4400 Project Phase 3
#group number 65
#Tyler Brown
#Gavin McWilliams
#Ananya Ghose
#Austin kinney

#this is the source code for the GUI required to do the heavy weight version
#of the project. We are building a database to aid the Atlanta Beltine project.

import Tkinter as tk
import tkFont
from Tkinter import IntVar
from Tkinter import StringVar
from PIL import ImageTk
from PIL import Image
import re


################################################################################
#code to make drawing widgets easier
################################################################################

OPTIONS = [
    'AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
    'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
    'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NC', 'ND', 'NE',
    'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI',
    'SC', 'SD', 'TN', 'TX', 'UM', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI',
    'WV', 'WY'
]

#class to act as a base for widgets
class base_widget(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)
        self.row = 0
        self.col = 0

    #function to draw the label on the screen
    def draw(self):
        self.grid(column=self.col, row=self.row, pady=5, padx=5)
        self.window.grid_rowconfigure(self.row, weight=1)
        self.window.grid_columnconfigure(self.col, weight=1)

    #function to change the row of a widget
    def set_row(self, new_row):
        self.row = new_row

    #function to change the column of a widget
    def set_col(self, new_col):
        self.col = new_col

    #method to center a button between a number of columnss
    def center(self, num_cols):
        self.grid(column=self.col, row=self.row, pady=5,
            padx=5, columnspan=num_cols)


#class to make drawing the title on a form easier
class title_text(tk.Frame):
    #parameters: window, the containing object
    #text: the title to display
    #num_cols: the number of columns in the form
    def __init__(self, window, text, num_cols):
        tk.Frame.__init__(self, window)
        #text in the title
        self.text = text
        #number of columns in the form
        self.num_cols = num_cols
        #the parent window
        self.window = window
        #create a font to use on the title
        arial18 = tkFont.Font(family='Arial', size=18, weight=tkFont.BOLD)
        #title is the name of the label object
        self.title = tk.Label(self, text=self.text, anchor="center",
            font=arial18, bg="white")
        #set up the label
        self.title.grid()
        #make window background white
        self.window.config(bg="white")

    #function to draw the title on the screen
    def draw(self):
        self.grid(columnspan=self.num_cols, pady=8, padx=8)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)


#class to make drawing labels on a form easier
class form_label(base_widget):
    #parameters: window, the containing object
    #text: the title to display
    #col: column position of the object
    #row: row position of the object
    def __init__(self, window, text, row, col):
        base_widget.__init__(self, window)
        #containing element of this label
        self.window = window
        #text for this label
        self.text = text
        #the row this label is in
        self.row = row
        #the column this label is in
        self.col = col
        #create a font to use on the title
        arial12 = tkFont.Font(family='Arial', size=12, weight=tkFont.BOLD)
        #label object for this class
        self.label = tk.Label(self, text=self.text, anchor="w",
            font=arial12, bg="white")
        #set up the label
        self.label.grid()


#class to make drawing buttons on a form easier
class form_button(base_widget):
    #parameters: window, the containing object
    #text: the title to display
    #col: column position of the object
    #row: row position of the object
    def __init__(self, window, text, row, col):
        base_widget.__init__(self, window)
        #containing element of this label
        self.window = window
        #text for this button
        self.text = text
        #the row this button is in
        self.row = row
        #the column this button is in
        self.col = col
        #create a font to use on the title
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #label object for this class
        self.button = tk.Button(self, text=self.text, anchor="center",
            font=arial10, bg="#4286f4", relief="flat", fg="white")
        #set up the button
        self.button.grid()

    #method to change button color
    def change_color(self, color):
        self.button.config(bg=color, fg="black", borderwidth=1)

    #method to attach a callback to the button
    def attach_callback(self, callback):
        self.button.config(command=callback)

    #method to adjust the width of a button
    def change_width(self, new_width):
        self.button.config(width=new_width)

    #change the text on the button
    def set_text(self, new_text):
        self.button.config(text=new_text)


#class to make drawing input boxes on a form easier
class form_entry(base_widget):
    #parameters: window, the containing object
    #text: the title to display
    #col: column position of the object
    #row: row position of the object
    def __init__(self, window, text, row, col):
        base_widget.__init__(self, window)
        #containing element of this label
        self.window = window
        #text for this input box
        self.text = text
        #the row this input box is in
        self.row = row
        #the column this input box is in
        self.col = col
        #create a font to use on the title
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #label object for this class
        self.entry = tk.Entry(self, textvariable=self.text, font=arial10,
            relief="sunken", borderwidth=2)
        #set up the input box
        self.entry.grid()

    #function to get the valaue entered
    def get_text(self):
        return self.entry.get()

    def clear(self):
        self.entry.delete(0, "end")

    #function to attach a validator to the entry object
    def attach_validator(self, validator):
        self.entry.config(validate="focus", validatecommand=validator)

#class to make drawing dropdown boxes on a form easier
class form_drop_down(base_widget):
    #parameters: window, the containing object
    #text: the title to display
    #col: column position of the object
    #row: row position of the object
    def __init__(self, window, row, col, options):
        base_widget.__init__(self, window)
        #containing element of this label
        self.window = window
        #text variable for this dropdown
        self.text = StringVar(window)
        self.text.set(options[0])
        #the row this dropdown is in
        self.row = row
        #the column this dropdown is in
        self.col = col
        #create a font to use on the title
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #options for the drop down box
        self.options = options
        #label object for this class
        arrow = ImageTk.PhotoImage(file='rsz_arrow_2.png')
        self.drop_down = tk.OptionMenu(self, self.text, *(self.options))
        self.drop_down.config(relief="flat", bg="white", font=arial10,
            indicatoron=0, compound='right', image=arrow,
            activebackground="white", borderwidth=2)
        self.drop_down.image = arrow
        #set up the dropdown
        self.drop_down.grid()

    #method to get the selected dropdown
    def get_text(self):
        return self.text.get()

    def set_options(self):
        self.drop_down.config(  )


#class to make drawing list boxes on a form easier
class form_list_box(base_widget):
    #parameters: window, the containing object
    #text: the title to display
    #col: column position of the object
    #row: row position of the object
    def __init__(self, window, row, col):
        base_widget.__init__(self, window)
        #containing element of this listbox
        self.window = window
        #the row this listbox is in
        self.row = row
        #the column this listbox is in
        self.col = col
        #create a font to use on the title
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #listbox object for this class
        self.listbox = tk.Listbox(self, font=arial10, height=3)
        #add scrollabars
        self.xscroll = tk.Scrollbar(self, relief="flat")
        self.xscroll.grid(row=0, column=1)
        #set up the dropdown
        self.listbox.grid(row=0, column=0)
        self.listbox.config(yscrollcommand=self.xscroll.set)
        self.xscroll.config(command=self.listbox.yview)

    def get_selected(self):
        return self.listbox.curselection()

    def delete_selected(self):
        temp = self.get_selected()
        if not temp:
            return
        else:
            for item in temp:
                self.listbox.delete(item)

    def delete_all(self):
        self.listbox.delete(0, "end")

    def add_item(self, item):
        self.listbox.insert("end", item)

    def get_all(self):
        return (self.listbox.get(0, "end"))

#class to represent a table
class form_table(base_widget):
    #parameters: num_cols, number of columns in the table
    #row, the row position of the table
    #col, the column position of the table
    #is_selectable, are the elements in the table selectable
    #window, the containing object
    def __init__(self, window, row, col, num_cols, is_selectable):
        base_widget.__init__(self, window)
        #containing element
        self.window = window
        #row position of this element
        self.row = row
        #column position of the element
        self.col = col
        #number of columns
        self.num_cols = num_cols
        #are the elements selectable
        self.is_selectable = is_selectable
        #create a font to use on the title
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #array to hold the columns
        self.columns = []
        #array to hold the column titles
        self.labels = []
        #array to hold the lsitboxes for items
        self.listboxes = []
        #frame that holds all of the table components
        self.master_frame = tk.Frame(self)
        self.master_frame.config(borderwidth=3)

        #loop to create the columns
        for i in range(num_cols):
            #frame to keep a column in
            temp_frame = tk.Frame(self.master_frame, bg="white", borderwidth=1, relief="groove")
            #push frames on to columns array
            self.columns.append(temp_frame)
            #make the title of each row
            temp_label = tk.Label(temp_frame, font=arial10, bg="white")
            #place the title
            temp_label.grid(row=0, column=0,)
            #store the title
            self.labels.append(temp_label)
            #make a listbox frame to hold listbox and scrollbar
            listbox_frame = tk.Frame(temp_frame, borderwidth=1, bg="white", relief="groove")
            listbox_frame.grid(row=1, column=0)
            #make the lsitbox for each column
            temp_listbox = tk.Listbox(listbox_frame, height=5, font=arial10, bg="white")
            temp_scroll = tk.Scrollbar(listbox_frame, relief="flat", bg="white", troughcolor="white")
            temp_listbox.grid(row=0, column=0)
            temp_scroll.grid(row=0, column=1)
            temp_listbox.config(yscrollcommand=temp_scroll.set)
            temp_scroll.config(command=temp_listbox.yview)
            if i == 0 and self.is_selectable:
                temp_listbox.config(state="normal")
            else:
                temp_listbox.config(state="disabled")

            #add the list box to the listbox array
            self.listboxes.append(temp_listbox)
            #add the frame to the master frame
            temp_frame.grid(row=0, column=i)

        #add master frame to the containing element
        self.master_frame.config(bg="white", borderwidth=1, relief="groove")
        self.master_frame.grid()


    def init_table(self, list_of_titles):
        for i in range(len(self.labels)):
            self.labels[i].config(text=list_of_titles[i])

    def append_row(self, row_tuple):
        for i in range(len(self.lsitboxes)):
            self.listboxes[i].insert(row_tuple[i])

    def delete_selected(self):
        temp = self.listboxes[0].get_selected()
        if not temp:
            return
        else:
            for item in temp:
                    self.listboxes[0].delete(item)

    def delete_all(self):
        for listbox in self.listboxes:
            listbox.delete(0, "end")


#class to represent a range input
class form_range(base_widget):
    def __init__(self, window, row, col):
        base_widget.__init__(self, window)
        #text vairables
        self.text1 = ""
        self.text2 = ""
        #keep track of the containing window
        self.window = window
        #row position
        self.row = row
        #column postion
        self.col = col
        #frame to contain everything
        self.master_frame = tk.Frame(self, bg="white")
        #define font
        arial10 = tkFont.Font(family='Arial', size=10, weight=tkFont.BOLD)
        #input boxes
        self.entry1 = tk.Entry(self.master_frame, textvariable=self.text1, font=arial10,
            relief="sunken", borderwidth=2, width=5)
        self.entry2 = tk.Entry(self.master_frame, textvariable=self.text2, font=arial10,
            relief="sunken", borderwidth=2, width=5)
        #label
        self.label = tk.Label(self.master_frame, text="--", bg="white", borderwidth=0)
        #add everything to the frame
        self.entry1.grid(row=0, column=0)
        self.entry2.grid(row=0, column=2)
        self.label.grid(row=0, column=1)

        self.master_frame.grid()

    def get_values(self):
        return (self.entry1.get(), self.entry2.get())

#class to represent a checkbox
class form_checkbox(base_widget):
    def __init__(self, window, text, row, col):
        base_widget.__init__(self, window)

        #keep track of the containining window
        self.window = window
        #row position
        self.row = row
        #column positoin
        self.col = col
        #text for the button
        self.text = text
        #is the checkbox selected
        self.is_checked = IntVar()
        #checkbox widget
        self.checkbox = tk.Checkbutton(self, text=self.text, variable=self.is_checked)

    def is_checked(self):
        if self.is_checked == 1:
            return True
        else:
            return False


################################################################################