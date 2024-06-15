import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from customtkinter import *
#--------------------------------------------#
#Calculate
def calculate_total():
    try:
        cost = float(cost_entry.get())
        tax = float(tax_entry.get())
        total = (cost * tax/100) + cost
        total_entry.delete(0, tk.END)
        total_entry.insert(0, total)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers for cost and tax.")
#--------------------------------------------#
window = Tk()
window.title('Motorbike Sales Management System')
window.geometry('750x750')
window.config(bg='lightgreen')
title_label = CTkLabel(window, text = 'MOTOBIKE SALES MANAGEMENT SYSTEM',text_color = 'tomato', font = ('Times new roman',20),fg_color = 'lightgreen').place(x = 200, y = 10)
day_label = CTkLabel(window, text = 'Day:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 100, y = 50)
type_label = CTkLabel(window, text = 'Type of motobike:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 60, y = 85)
cost_label = CTkLabel(window, text = 'Cost:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 100, y = 120)
staff_label = CTkLabel(window, text = 'Staff:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 450, y = 50)
tax_label = CTkLabel(window, text = 'Tax:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 450, y = 85)
total_label = CTkLabel(window, text = 'Total:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 450, y = 120)
color_label = CTkLabel(window, text = 'Color:',text_color = 'tomato',font=('Times new roman',18),fg_color = 'lightgreen').place(x = 250, y = 155)
#Entry
cost_entry = CTkEntry(window,corner_radius = 32,border_color = 'hotpink')
cost_entry.place(x = 200, y = 120)
tax_entry = CTkEntry(window,corner_radius = 32,border_color = 'hotpink')
tax_entry.place(x = 500, y = 85)
total_entry = CTkEntry(window,corner_radius = 32,border_color = 'hotpink')
total_entry.place(x = 500, y = 120)
#Combobox
staff_combobox = CTkComboBox(window,values = ['','Phạm Quang Khải', 'Phạm Quang', 'Phạm'], fg_color = 'lightpink',border_color = 'hotpink', dropdown_fg_color = 'lightpink',corner_radius = 32)
staff_combobox.place(x = 500, y = 50)
type_combobox = CTkComboBox(window,values = ['','Peugeot Scooter', 'Scoopy', 'SH','Air Blade','SH Mode','Vision'], fg_color = 'lightpink',border_color = 'hotpink', dropdown_fg_color = 'lightpink',corner_radius = 32)
type_combobox.place(x = 200, y = 85)
color_combobox = CTkComboBox(window,values = ['','Red', 'Blue', 'Pink', 'Black', 'White', 'Green'], fg_color = 'lightpink',border_color = 'hotpink', dropdown_fg_color = 'lightpink',corner_radius = 32)
color_combobox.place(x = 300, y = 155)
#Date_Entry
day_entry = DateEntry(window,background='salmon',date_pattern='MM/dd/yyyy')
day_entry.place(x = 200, y = 50)
#Button
calculate_button = CTkButton(window, text = 'CALCULATE',corner_radius = 32,command= calculate_total, fg_color="hotpink",width=40, height=25)
calculate_button.place(x=650, y=120)
save_button = CTkButton(window, text = 'SAVE',corner_radius = 32, fg_color="hotpink",width=30, height=25)
save_button.place(x = 450, y = 200)

#Table
style = ttk.Style()
style.configure('Treeview',background = 'darkgrey',foreground = 'black',rowheight = 25, fieldbackground = 'darkgrey')
style.map('Treeview',background = [('selected','lightpink')])
table = ttk.Treeview(window,column = ('ID','Day', 'Type of motobike','Cost','Staff','Tax','Total'),show = 'headings')
table.heading('ID',text = 'ID')
table.heading('Day', text = 'Day')
table.heading('Type of motobike', text = 'Type of motobike')
table.heading('Cost', text = 'Cost (VND)')
table.heading('Staff', text = 'Staff')
table.heading('Tax', text = 'Tax (%)')
table.heading('Total', text = 'Total (VND)')
table.column('ID',width = 30)
table.column('Day', width=100)
table.column('Type of motobike', width=125)
table.column('Cost', width=125)
table.column('Staff', width=125)
table.column('Tax', width=75)
table.column('Total', width=125)
table.place(x = 20, y = 250)

#Add
add_button = CTkButton(window, text = 'ADD',corner_radius = 32,command=lambda: add_data(), fg_color="hotpink",width=30, height=25)
add_button.place(x = 250, y = 200)
i = 0
def add_data():
    day = day_entry.get()
    type_of_motobike = type_combobox.get()
    cost = cost_entry.get()
    staff = staff_combobox.get()
    tax = tax_entry.get()
    total = float(cost) * float(tax)
    global i
    i += 1
    table.insert("", 'end', values=(i, day, type_of_motobike, cost, staff, tax, total))

    day_entry.delete(0, tk.END)
    type_combobox.set('')
    cost_entry.delete(0, tk.END)
    staff_combobox.set('')
    tax_entry.delete(0, tk.END)
    total_entry.delete(0, tk.END)
    day_entry.focus()
    messagebox.showinfo("Success", "Data added successfully!")
#Delete
delete_button = CTkButton(window, text = 'DELETE',corner_radius = 32,command=lambda: delete_data(), fg_color="hotpink",width=40, height=25)
delete_button.place(x = 350, y = 200)
def delete_data():
    selected_row = table.selection()
    if selected_row:
        table.delete(selected_row[0])
    messagebox.showinfo("Success", "Data deleted successfully!")

window.mainloop()
