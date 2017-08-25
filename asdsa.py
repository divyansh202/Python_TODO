# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:04:02 2017

@author: Divyansh Shukla
"""

import tkinter
import tkinter.messagebox
import random
import sqlite3

conn = sqlite3.connect('todo.db')
c = conn.cursor()



root = tkinter.Tk()

root.configure(bg="white")

root.title("To Do List")

root.geometry("240x220")

tasks = []

def data_entry(task):
    c.execute("INSERT INTO Tasks VALUES('task','')")
    conn.commit()
    
    
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Tasks(Fin_task TEXT, Unfin_task TEXT)")

def read_from_db():
    c.execute('SELECT * FROM Tasks')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)


def update_listbox():
	clear_listbox()
	for task in tasks:
		lb_tasks.insert("end", task)

def clear_listbox():
	lb_tasks.delete(0, "end")

def add_task():
    create_table()
    task = txt_input.get()
    if task !="":
        tasks.append(task)
        data_entry(task)
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter a task.")
    txt_input.delete(0, "end")
		
def del_all():
	confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all?")
	if confirmed == True:
		global tasks
		tasks = []
		update_listbox()

def del_one():
	task = lb_tasks.get("active")
	if task in tasks:
		tasks.remove(task)
	update_listbox()

def sort_asc():
	tasks.sort()
	update_listbox()

def sort_desc():
	tasks.sort()
	tasks.reverse()
	update_listbox()
    
def endProgam():
    root.destroy()
    
def choose_random():
	task = random.choice(tasks)
	lbl_display["text"]=task

def show_number_of_tasks():
	number_of_tasks = len(tasks)
	msg = "Number of tasks: %s" %number_of_tasks
	lbl_display["text"]=msg


lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="Sort (DESC)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)
'''
btn_choose_random = tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.grid(row=6,column=0)
'''
btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg="green", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=6,column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", command=endProgam)
btn_exit.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="Show", fg="green", bg="white", command=read_from_db)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root, bg="red")
lb_tasks.grid(row=2,column=1, rowspan=10)

root.mainloop()