#CS 4400 Project Phase 3
#group number 65
#Tyler Brown
#Gavin McWilliams
#Ananya Ghose
#Austin kinney

#this is the source code for the GUI required to do the heavy weight version
#of the project. We are building a database to aid the Atlanta Beltine project.
from gui import *
import MySQLdb


################################################################################
#code for making the individual screens to be displayed
################################################################################

previous_screen = 1

#login screen
class screen_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add the title of the screen
        self.title = title_text(self, "Atlanta Beltine Login", 2)
        self.title.draw()

        #add the labels
        self.label1 = form_label(self, "Email", 1, 0)
        self.label2 = form_label(self, "Password", 2, 0)
        self.label1.draw()
        self.label2.draw()

        #add the input boxes
        self.input1 = form_entry(self, "Email", 1, 1)
        self.input2 = form_entry(self, "Password", 2, 1)
        self.input1.draw()
        self.input2.draw()

        #add the buttons
        self.button1 = form_button(self, "Login", 3, 0)
        self.button2 = form_button(self, "Register", 3, 1)
        self.button1.change_width(20)
        self.button2.change_width(20)
        self.button1.attach_callback(self.login)
        self.button2.attach_callback(lambda: self.next_screen(2))
        self.button1.draw()
        self.button2.draw()

    def login(self):
        self.controller.show_frame(screen_10)

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 1
        self.controller.show_frame(determine_screen(index))


#register navigation screen
class screen_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Register Navigation", 1)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "User Only", 1, 0)
        self.button1.change_width(20)
        self.button1.attach_callback(lambda: self.next_screen(3))
        self.button1.draw()
        self.button2 = form_button(self, "Visitor Only", 2, 0)
        self.button2.attach_callback(lambda: self.next_screen(4))
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Employee Only", 3, 0)
        self.button3.attach_callback(lambda: self.next_screen(5))
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Employee-Visitor", 4, 0)
        self.button4.attach_callback(lambda: self.next_screen(6))
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "Back", 5, 0)
        self.button5.change_width(20)
        self.button5.attach_callback(lambda: self.prev_screen())
        self.button5.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen(1))


    def next_screen(self, index):
        global previous_screen
        previous_screen = 2
        self.controller.show_frame(determine_screen(index))


#base class for adding people

#register user screen
class screen_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #save the controller
        self.controller = controller

        #add title
        self.title = title_text(self, "Register User", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "First Name", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Last Name", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Username", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Password", 3, 0)
        self.label4.draw()
        self.label5 = form_label(self, "Confirm Password", 3, 2)
        self.label5.draw()
        self.label6 = form_label(self, "Email", 4, 0)
        self.label6.draw()

        #add input boxes
        self.input1 = form_entry(self, "First Name", 1, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "Last Name", 1, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Username", 2, 1)
        self.input3.draw()
        self.input4 = form_entry(self, "Password", 3, 1)
        self.input4.draw()
        self.input5 = form_entry(self, "Confirm Password", 3, 3)
        self.input5.draw()

        #add buttons
        self.button1 = form_button(self, "Back", 6, 0)
        self.button1.attach_callback(self.prev_screen)
        self.button1.change_width(10)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Register", 6, 2)
        self.button2.change_width(10)
        self.button2.center(2)
        self.button2.draw()

        #add list box widget
        self.listbox = form_list_box(self, 4, 1)
        self.listbox.draw()

        #add remove button
        self.remove_button = form_button(self, "Remove", 4, 2)
        self.remove_button.change_color("grey")
        self.remove_button.attach_callback(self.remove_items)
        self.remove_button.change_width(10)
        self.remove_button.draw()

        #add in initial row of controls
        self.add_input = form_entry(self, "Email", 5, 1)
        self.add_button = form_button(self, "Add", 5, 2)
        self.add_button.change_width(10)
        self.add_button.change_color("grey")
        self.add_button.attach_callback(self.add_new_item)
        self.add_input.draw()
        self.add_button.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 3
        self.controller.show_frame(determine_screen(index))


    def add_new_item(self):
        if self.email_validator():
            self.listbox.add_item(self.add_input.get_text())
            self.add_input.clear()


    def remove_items(self):
        self.listbox.delete_selected()

    def clear(self):
        self.listbox.delete_all()
        self.add_input.clear()

    def email_validator(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.add_input.get_text()):
            return False

        return True


#register visitor screen
class screen_4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #save the controller
        self.controller = controller

        #add title
        self.title = title_text(self, "Register Visitor", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "First Name", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Last Name", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Username", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Password", 3, 0)
        self.label4.draw()
        self.label5 = form_label(self, "Confirm Password", 3, 2)
        self.label5.draw()
        self.label6 = form_label(self, "Email", 4, 0)
        self.label6.draw()

        #add input boxes
        self.input1 = form_entry(self, "First Name", 1, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "Last Name", 1, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Username", 2, 1)
        self.input3.draw()
        self.input4 = form_entry(self, "Password", 3, 1)
        self.input4.draw()
        self.input5 = form_entry(self, "Confirm Password", 3, 3)
        self.input5.draw()

        #add buttons
        self.button1 = form_button(self, "Back", 6, 0)
        self.button1.attach_callback(self.prev_screen)
        self.button1.change_width(10)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Register", 6, 2)
        self.button2.change_width(10)
        self.button2.center(2)
        self.button2.draw()

        #add list box widget
        self.listbox = form_list_box(self, 4, 1)
        self.listbox.draw()

        #add remove button
        self.remove_button = form_button(self, "Remove", 4, 2)
        self.remove_button.change_color("grey")
        self.remove_button.attach_callback(self.remove_items)
        self.remove_button.change_width(10)
        self.remove_button.draw()

        #add in initial row of controls
        self.add_input = form_entry(self, "Email", 5, 1)
        self.add_button = form_button(self, "Add", 5, 2)
        self.add_button.change_width(10)
        self.add_button.change_color("grey")
        self.add_button.attach_callback(self.add_new_item)
        self.add_input.draw()
        self.add_button.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 4
        self.controller.show_frame(determine_screen(index))

    def add_new_item(self):
        if self.email_validator():
            self.listbox.add_item(self.add_input.get_text())
            self.add_input.clear()


    def remove_items(self):
        self.listbox.delete_selected()

    def clear(self):
        self.listbox.delete_all()
        self.add_input.clear()

    def email_validator(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.add_input.get_text()):
            return False

        return True


#register employee screen
class screen_5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #save the controller
        self.controller = controller

        #add title
        self.title = title_text(self, "Register Employee", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "First Name", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Last Name", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Username", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Password", 3, 0)
        self.label4.draw()
        self.label5 = form_label(self, "Confirm Password", 3, 2)
        self.label5.draw()
        self.label6 = form_label(self, "Email", 4, 0)
        self.label6.draw()
        self.label7 = form_label(self, "User Type", 2, 2)
        self.label7.draw()
        self.label8 = form_label(self, "Address", 4, 2)
        self.label8.draw()
        self.label9 = form_label(self, "Phone", 4, 0)
        self.label9.draw()
        self.label10 = form_label(self, "City", 5, 0)
        self.label10.draw()
        self.label11 = form_label(self, "Zipcode", 5, 2)
        self.label11.draw()
        self.label12 = form_label(self, "State", 6, 1)
        self.label12.draw()
        self.label13 = form_label(self, "Email", 7, 0)
        self.label13.draw()

        #add input boxes
        self.input1 = form_entry(self, "First Name", 1, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "Last Name", 1, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Username", 2, 1)
        self.input3.draw()
        self.input4 = form_entry(self, "Password", 3, 1)
        self.input4.draw()
        self.input5 = form_entry(self, "Confirm Password", 3, 3)
        self.input5.draw()
        self.input7 = form_entry(self, "Phone", 4, 1)
        self.input8 = form_entry(self, "Address", 4, 3)
        self.input9 = form_entry(self, "City", 5, 1)
        self.input10 = form_entry(self, "Zipcode", 5, 3)
        self.input7.draw()
        self.input8.draw()
        self.input9.draw()
        self.input10.draw()

        #add drop down boxes
        self.employee_options = [
            "Manager",
            "Staff"
        ]

        self.dropdown1 = form_drop_down(self, 2, 3, self.employee_options)
        self.dropdown2 = form_drop_down(self, 6, 2, OPTIONS)
        self.dropdown1.draw()
        self.dropdown2.draw()

        #add buttons
        self.button1 = form_button(self, "Back", 9, 0)
        self.button1.attach_callback(self.prev_screen)
        self.button1.change_width(10)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Register", 9, 2)
        self.button2.change_width(10)
        self.button2.center(2)
        self.button2.draw()

        #add list box widget
        self.listbox = form_list_box(self, 7, 1)
        self.listbox.draw()

        #add remove button
        self.remove_button = form_button(self, "Remove", 7, 2)
        self.remove_button.change_color("grey")
        self.remove_button.attach_callback(self.remove_items)
        self.remove_button.change_width(10)
        self.remove_button.draw()

        #add in initial row of controls
        self.add_input = form_entry(self, "Email", 8, 1)
        self.add_button = form_button(self, "Add", 8, 2)
        self.add_button.change_width(10)
        self.add_button.change_color("grey")
        self.add_button.attach_callback(self.add_new_item)
        self.add_input.draw()
        self.add_button.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 5
        self.controller.show_frame(determine_screen(index))

    def add_new_item(self):
        if self.email_validator():
            self.listbox.add_item(self.add_input.get_text())
            self.add_input.clear()


    def remove_items(self):
        self.listbox.delete_selected()

    def clear(self):
        self.listbox.delete_all()
        self.add_input.clear()

    def email_validator(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.add_input.get_text()):
            return False

        return True

#register employee-visitor screen
class screen_6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #save the controller
        self.controller = controller

        #add title
        self.title = title_text(self, "Register Employee-Visitor", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "First Name", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Last Name", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Username", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Password", 3, 0)
        self.label4.draw()
        self.label5 = form_label(self, "Confirm Password", 3, 2)
        self.label5.draw()
        self.label6 = form_label(self, "Email", 4, 0)
        self.label6.draw()
        self.label7 = form_label(self, "User Type", 2, 2)
        self.label7.draw()
        self.label8 = form_label(self, "Address", 4, 2)
        self.label8.draw()
        self.label9 = form_label(self, "Phone", 4, 0)
        self.label9.draw()
        self.label10 = form_label(self, "City", 5, 0)
        self.label10.draw()
        self.label11 = form_label(self, "Zipcode", 5, 2)
        self.label11.draw()
        self.label12 = form_label(self, "State", 6, 1)
        self.label12.draw()
        self.label13 = form_label(self, "Email", 7, 0)
        self.label13.draw()

        #add input boxes
        self.input1 = form_entry(self, "First Name", 1, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "Last Name", 1, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Username", 2, 1)
        self.input3.draw()
        self.input4 = form_entry(self, "Password", 3, 1)
        self.input4.draw()
        self.input5 = form_entry(self, "Confirm Password", 3, 3)
        self.input5.draw()
        self.input7 = form_entry(self, "Phone", 4, 1)
        self.input8 = form_entry(self, "Address", 4, 3)
        self.input9 = form_entry(self, "City", 5, 1)
        self.input10 = form_entry(self, "Zipcode", 5, 3)
        self.input7.draw()
        self.input8.draw()
        self.input9.draw()
        self.input10.draw()

        #add drop down boxes
        self.employee_options = [
            "Manager",
            "Staff"
        ]

        self.dropdown1 = form_drop_down(self, 2, 3, self.employee_options)
        self.dropdown2 = form_drop_down(self, 6, 2, OPTIONS)
        self.dropdown1.draw()
        self.dropdown2.draw()

        #add buttons
        self.button1 = form_button(self, "Back", 9, 0)
        self.button1.attach_callback(self.prev_screen)
        self.button1.change_width(10)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Register", 9, 2)
        self.button2.change_width(10)
        self.button2.center(2)
        self.button2.draw()

        #add list box widget
        self.listbox = form_list_box(self, 7, 1)
        self.listbox.draw()

        #add remove button
        self.remove_button = form_button(self, "Remove", 7, 2)
        self.remove_button.change_color("grey")
        self.remove_button.attach_callback(self.remove_items)
        self.remove_button.change_width(10)
        self.remove_button.draw()

        #add in initial row of controls
        self.add_input = form_entry(self, "Email", 8, 1)
        self.add_button = form_button(self, "Add", 8, 2)
        self.add_button.change_width(10)
        self.add_button.change_color("grey")
        self.add_button.attach_callback(self.add_new_item)
        self.add_input.draw()
        self.add_button.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 6
        self.controller.show_frame(determine_screen(index))

    def add_new_item(self):
        if self.email_validator():
            self.listbox.add_item(self.add_input.get_text())
            self.add_input.clear()


    def remove_items(self):
        self.listbox.delete_selected()

    def clear(self):
        self.listbox.delete_all()
        self.add_input.clear()

    def email_validator(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.add_input.get_text()):
            return False

        return True

#user functionality screen
class screen_7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add a title
        self.title = title_text(self, "User Functionality", 1)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Take Transit", 1, 0)
        self.button1.attach_callback(lambda: self.next_screen(15))
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "View Transit History", 2, 0)
        self.button2.attach_callback(lambda: self.next_screen(16))
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Back", 3, 0)
        self.button3.attach_callback(lambda: self.prev_screen())
        self.button3.change_width(20)
        self.button3.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 7
        self.controller.show_frame(determine_screen(index))


#Administrator-only functionality screen
class screen_8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Administrator Functionality", 2)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Take Transit", 1, 1)
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "View Transit History", 2, 1)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Back", 3, 1)
        self.button3.attach_callback(lambda: self.prev_screen())
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Manage Profile", 1, 0)
        self.button4.attach_callback(lambda: self.next_screen(17))
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "Manage User", 2, 0)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "Manage Transit", 3, 0)
        self.button6.change_width(20)
        self.button6.draw()
        self.button7 = form_button(self, "Manage Site", 4, 0)
        self.button7.change_width(20)
        self.button7.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 8
        self.controller.show_frame(determine_screen(index))

#Administrator-visitor functionality screen
class screen_9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Administrator Functionality", 2)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Take Transit", 2, 1)
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "View Transit History", 5, 0)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Back", 5, 1)
        self.button3.attach_callback(lambda: self.prev_screen())
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Manage Profile", 1, 0)
        self.button4.attach_callback(lambda: self.next_screen(17))
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "Manage User", 1, 1)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "Manage Transit", 2, 0)
        self.button6.change_width(20)
        self.button6.draw()
        self.button7 = form_button(self, "Manage Site", 3, 0)
        self.button7.change_width(20)
        self.button7.draw()
        self.button8 = form_button(self, "Explore Event", 4, 0)
        self.button8.change_width(20)
        self.button8.draw()
        self.button9 = form_button(self, "Explore Site", 3, 1)
        self.button9.change_width(20)
        self.button9.draw()
        self.button10 = form_button(self, "View Visit History", 4, 1)
        self.button10.change_width(20)
        self.button10.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 9
        self.controller.show_frame(determine_screen(index))

#Manager-only functionality page
class screen_10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Manager Functionality", 2)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Manage Profile", 1, 0)
        self.button1.attach_callback(lambda: self.next_screen(17))
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "Manage Event", 2, 0)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "View Staff", 3, 0)
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Back", 4, 0)
        self.button4.attach_callback(lambda: self.prev_screen())
        self.button4.change_width(20)
        self.button4.center(2)
        self.button4.draw()
        self.button5 = form_button(self, "Take Transit", 2, 1)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "View Transit History", 3, 1)
        self.button6.change_width(20)
        self.button6.draw()
        self.button7 = form_button(self, "View Site Report", 1, 1)
        self.button7.change_width(20)
        self.button7.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen(1))


    def next_screen(self, index):
        global previous_screen
        previous_screen = 10
        self.controller.show_frame(determine_screen(index))

#Manager-visitor functionality page
class screen_11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Manager Functionality", 2)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Manage Profile", 1, 0)
        self.button1.attach_callback(lambda: controller.show_frame(screen_17))
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "Manage Event", 1, 1)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "View Staff", 2, 0)
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Back", 5, 1)
        self.button4.attach_callback(lambda: self.prev_screen())
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "Take Transit", 4, 0)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "View Transit History", 4, 1)
        self.button6.change_width(20)
        self.button6.draw()
        self.button7 = form_button(self, "View Site Report", 2, 1)
        self.button7.change_width(20)
        self.button7.draw()
        self.button8 = form_button(self, "View Visit History", 5, 0)
        self.button8.change_width(20)
        self.button8.draw()
        self.button9 = form_button(self, "Explore Event", 3, 1)
        self.button9.change_width(20)
        self.button9.draw()
        self.button10 = form_button(self, "Explore Site", 3, 0)
        self.button10.change_width(20)
        self.button10.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 11
        self.controller.show_frame(determine_screen(index))

#staff-only functionality page
class screen_12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Staff Functionality", 1)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Manage Profile", 1, 0)
        self.button1.attach_callback(lambda: self.next_screen(17))
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "View Schedule", 2, 0)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Back", 5, 0)
        self.button3.attach_callback(lambda: self.prev_screen())
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Take Transit", 3, 0)
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "View Transit History", 4, 0)
        self.button5.change_width(20)
        self.button5.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 12
        self.controller.show_frame(determine_screen(index))

#staff-visitor functionality page
class screen_13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Staff Functionality", 2)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Manage Profile", 1, 0)
        self.button1.attach_callback(lambda: self.next_screen(17))
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "View Schedule", 2, 0)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "Back", 4, 1)
        self.button3.attach_callback(lambda: self.prev_screen())
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Take Transit", 3, 0)
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "View Transit History", 4, 0)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "Explore Event", 1, 1)
        self.button6.change_width(20)
        self.button6.draw()
        self.button7 = form_button(self, "Explore Site", 2, 1)
        self.button7.change_width(20)
        self.button7.draw()
        self.button8 = form_button(self, "View Visit History", 3, 1)
        self.button8.change_width(20)
        self.button8.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 13
        self.controller.show_frame(determine_screen(index))



#visitor only functionality page
class screen_14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Visitor Functionality", 1)
        self.title.draw()

        #add buttons
        self.button1 = form_button(self, "Back", 6, 0)
        self.button1.attach_callback(lambda: self.prev_screen())
        self.button1.change_width(20)
        self.button1.draw()
        self.button2 = form_button(self, "Take Transit", 4, 0)
        self.button2.change_width(20)
        self.button2.draw()
        self.button3 = form_button(self, "View Transit History", 5, 0)
        self.button3.change_width(20)
        self.button3.draw()
        self.button4 = form_button(self, "Explore Event", 1, 0)
        self.button4.change_width(20)
        self.button4.draw()
        self.button5 = form_button(self, "Explore Site", 2, 0)
        self.button5.change_width(20)
        self.button5.draw()
        self.button6 = form_button(self, "View Visit History", 3, 0)
        self.button6.change_width(20)
        self.button6.draw()

    def prev_screen(self):
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 14
        self.controller.show_frame(determine_screen(index))

#User Take Transit
class screen_15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Take Transit", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "Contain Site", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Transport Type", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Price Range", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Transit Date", 4, 1)
        self.label4.draw()

        #add dropdown boxes
        self.site_options = ["Inman Park"]
        self.dropdown1 = form_drop_down(self, 1, 1, self.site_options)
        self.dropdown1.draw()
        self.transport_options = ["ALL", "MARTA", "Bus", "Bike"]
        self.dropdown2 = form_drop_down(self, 1, 3, self.transport_options)
        self.dropdown2.draw()

        #add buttons
        self.button1 = form_button(self, "Filter", 2, 2)
        self.button1.change_width(15)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Back", 4, 0)
        self.button2.change_width(15)
        self.button2.attach_callback(self.prev_screen)
        self.button2.draw()
        self.button3 = form_button(self, "Log Transit", 4, 3)
        self.button3.change_width(15)
        self.button3.draw()

        #input boxes
        self.input1 = form_entry(self, "Transit Date", 4, 2)
        self.input1.draw()

        #range widget
        self.range1 = form_range(self, 2, 1)
        self.range1.draw()

        #table widget
        self.table1 = form_table(self, 3, 0, 4, True)
        self.table1.center(4)
        self.table1.init_table(["Route", "Transport Type", "Price", "# Connected Sites"])
        self.table1.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 15
        self.controller.show_frame(determine_screen(index))

    def clear(self):
        self.table1.delete_all()
        self.input1.clear()

#User transit history
class screen_16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #add title
        self.title = title_text(self, "Transit History", 4)
        self.title.draw()

        #add labels
        self.label1 = form_label(self, "Contain Site", 1, 2)
        self.label1.draw()
        self.label2 = form_label(self, "Transport Type", 1, 0)
        self.label2.draw()
        self.label3 = form_label(self, "Route", 2, 1)
        self.label3.draw()
        self.label4 = form_label(self, "Start Date", 3, 0)
        self.label4.draw()
        self.label5 = form_label(self, "End Date", 3, 2)
        self.label5.draw()

        #add dropdown boxes
        self.site_options = ["Inman Park"]
        self.dropdown1 = form_drop_down(self, 1, 3, self.site_options)
        self.dropdown1.draw()
        self.transport_options = ["ALL", "MARTA", "Bus", "Bike"]
        self.dropdown2 = form_drop_down(self, 1, 1, self.transport_options)
        self.dropdown2.draw()

        #add buttons
        self.button1 = form_button(self, "Filter", 4, 1)
        self.button1.change_width(15)
        self.button1.center(2)
        self.button1.draw()
        self.button2 = form_button(self, "Back", 6, 0)
        self.button2.change_width(15)
        self.button2.center(4)
        self.button2.attach_callback(self.prev_screen)
        self.button2.draw()

        #input boxes
        self.input1 = form_entry(self, "Start Date", 3, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "End Date", 3, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Route", 2, 2)
        self.input3.draw()

        #table widget
        self.table1 = form_table(self, 5, 0, 4, False)
        self.table1.center(4)
        self.table1.init_table(["Date", "Route", "Transport Type", "Price"])
        self.table1.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 6
        self.controller.show_frame(determine_screen(index))

    def clear(self):
        self.table1.delete_all()
        self.input1.clear()
        self.input2.clear()
        self.input3.clear()

#Employee Manage Profile
class screen_17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #title
        self.title = title_text(self, "Manage Profile", 4)
        self.title.draw()

        #labels
        self.label1 = form_label(self, "First Name", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Last Name", 1, 2)
        self.label2.draw()
        self.label3 = form_label(self, "Username", 2, 0)
        self.label3.draw()
        self.label4 = form_label(self, "Site Name", 2, 2)
        self.label4.draw()
        self.label5 = form_label(self, "Employee ID", 3, 0)
        self.label5.draw()
        self.label6 = form_label(self, "Phone", 3, 2)
        self.label6.draw()
        self.label7 = form_label(self, "Address", 4, 1)
        self.label7.draw()
        self.label8 = form_label(self, "Email", 5, 0)
        self.label8.draw()
        self.label9 = form_label(self, "username 2", 2, 1)
        self.label9.draw()
        self.label10 = form_label(self, "site name 2", 2, 3)
        self.label10.draw()
        self.label11 = form_label(self, "employee id 2", 3, 1)
        self.label11.draw()
        self.label12 = form_label(self, "address 2", 4, 2)
        self.label12.draw()

        #list box
        self.listbox = form_list_box(self, 5, 1)
        self.listbox.draw()

        #buttons
        self.button1 = form_button(self, "Remove", 5, 2)
        self.button1.attach_callback(self.remove_items)
        self.button1.change_color("grey")
        self.button1.draw()
        self.button2 = form_button(self, "Add", 6, 2)
        self.button2.attach_callback(self.add_new_item)
        self.button2.change_color("grey")
        self.button2.draw()
        self.button3 = form_button(self, "Back", 8, 2)
        self.button3.attach_callback(self.prev_screen)
        self.button3.change_width(15)
        self.button3.draw()
        self.button4 = form_button(self, "Update", 8, 1)
        self.button4.change_width(15)
        self.button4.draw()

        #inputs
        self.input1 = form_entry(self, "First Name", 1, 1)
        self.input1.draw()
        self.input2 = form_entry(self, "Last Name", 1, 3)
        self.input2.draw()
        self.input3 = form_entry(self, "Phone", 3, 3)
        self.input3.draw()
        self.input4 = form_entry(self, "Email", 6, 1)
        self.input4.draw()

        #check box
        self.check_box = form_checkbox(self, "Visitor Account", 7, 0)
        self.check_box.center(4)
        self.check_box.draw()

    def prev_screen(self):
        self.clear()
        self.controller.show_frame(determine_screen())


    def next_screen(self, index):
        global previous_screen
        previous_screen = 15
        self.controller.show_frame(determine_screen(index))


    def add_new_item(self):
        if self.email_validator():
            self.listbox.add_item(self.input4.get_text())
            self.input4.clear()


    def remove_items(self):
        self.listbox.delete_selected()

    def clear(self):
        self.listbox.delete_all()
        self.input4.clear()

    def email_validator(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.input4.get_text()):
            return False

        return True


#manage user screen
class screen_18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        #title
        self.title = title_text(self, "Manage User", 4)

        #labels
        self.label1 = form_label(self, "Username", 1, 0)
        self.label1.draw()
        self.label2 = form_label(self, "Type", 1, 2)
        self.label3.draw()
        self.label4 = form_label(self, "Status", 2, 1)
        self.label4.draw()

        #input boxes
        self.input1 = form_entry(self, "Username", 1, 1)
        self.input1.draw()

        #buttons
        self.button1 = form_button(self, "Filter", 3, 1)
        self.button1.draw()
        self.button2 = form_button(self, "Approve", 3, 2)
        self.button2.draw()
        self.button3 = form_button(self, "Decline", 3, 3)
        self.button3.draw()
        self.button4 = form_button(self, "Back", 5, 0)
        self.button4.center(4)
        self.button4.draw()

        #dropdown boxes
        self.type_options = ["User", "Visitor", "Staff", "Manager"]
        self.status_options = ["Approved", "Pending", "Declined"]
        self.dropdown1 = form_drop_down(self, 1, 3, self.type_options)
        self.dropdown1.draw()
        self.dropdown2 = form_drop_down(self, 2, 2, self.status_options)
        self.dropdown2.draw()

        #table
        self.table = form_table(self, 4, 0, 4, True)
        self.table.center(4)
        self.table.draw()


################################################################################

FRAMES = [
    screen_1,
    screen_2,
    screen_3,
    screen_4,
    screen_5,
    screen_6,
    screen_7,
    screen_8,
    screen_9,
    screen_10,
    screen_11,
    screen_12,
    screen_13,
    screen_14,
    screen_15,
    screen_16,
    screen_17
]

def determine_screen(screen=-100):
    global previous_screen
    if screen < 0:
        screen = previous_screen
    return FRAMES[screen - 1]

################################################################################
#screen manager class and the mainloop
################################################################################

#class to manage and change the screens when need be
class database_app(tk.Tk):
     def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (FRAMES):
             frame = F(container, self)

             self.frames[F] = frame

             frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame(FRAMES[0])

     def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


app = database_app()
app.title("Atlanta Beltine")
app.wm_iconbitmap('gatech.ico')

app.mainloop()

###############################end script#######################################