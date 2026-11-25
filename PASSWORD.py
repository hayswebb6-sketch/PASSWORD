import secrets 
from time import perf_counter
import string
import random as rand
import tkinter as tk
from tkinter import messagebox as msg, filedialog as fd, ttk
from pyperclip import copy
character="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
special="!@#$%^&*()_+|}{:<>?`~"
digit="1234567890"
guesses=0
def make_password():
    allowed_chars=""
    try:
        character_amt=int(password_length.get().strip())
    except ValueError:
        msg.showerror("Error","Please enter a number")
        return
    if character_amt<=0:
        msg.showerror("Error","Please enter a number greater than 0")
        return
    if special_var.get()==True:
        allowed_chars+=special
    if character_var.get()==True:
        allowed_chars+=character
    if digit_var.get()==True:
        allowed_chars+=digit
    if allowed_chars:
        password="".join(secrets.choice(allowed_chars) for _ in range(character_amt))
    else:
        msg.showerror("Error","Please select at least one option")
        return
    password_entry.configure(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.configure(state="disabled", disabledforeground="white", disabledbackground="black")
def brute_force():
    global users_password
    users_password=brute_password.get()
    if check_if_digit()==True and check_if_symbol()==False:
        brute_password_digits_pre()
    elif check_if_digit()==False and check_if_symbol()==True:
        brute_password_with_special_pre()
    elif check_if_digit()==True and check_if_symbol()==True:
        brute_password_special_digits_pre()
    else:
        brute_password_normal_pre()
def check_if_digit():
    if any(char.isdigit() for char in users_password):
        return True
    else:
        return False
def check_if_symbol():
    if any(char in string.punctuation for char in users_password):
        return True
    else:
        return False
def brute_password_with_special_pre():
    global guesses
    global users_password
    password_length=len(users_password)
    start_time=perf_counter()
    
    def brute_password_with_special():
        password="".join(rand.choices(character+special,k=password_length))
        guesses+=1
        if password==users_password:
            
            end_time=perf_counter()
            elapsed_time=end_time-start_time
            brute_log.config(state="normal")
            brute_log.insert("end",f"\nPassword found. It is {password}\nIt was found in {elapsed_time:.2f} seconds with {guesses} guesses.\n")
            brute_log.see("end")
            brute_log.config(state="disabled")
            guesses=0
        else:
            root.after(1,brute_password_with_special)
    brute_password_with_special()
def brute_password_normal_pre():
    global guesses
    global users_password
    password_length=len(users_password)
    start_time=perf_counter()
    
    def brute_password_normal():
        global guesses
        password="".join(rand.choices(character,k=password_length))
        guesses+=1
        if password==users_password:
            
            end_time=perf_counter()
            elapsed_time=end_time-start_time
            brute_log.config(state="normal")
            brute_log.insert("end",f"\nPassword found. It is {password}\nIt was found in {elapsed_time:.2f} seconds with {guesses} guesses.\n")
            brute_log.see("end")
            brute_log.config(state="disabled")
            guesses=0
        else:
            root.after(1, brute_password_normal)
    brute_password_normal()
def brute_password_digits_pre():
    global guesses
    global users_password
    password_length=len(users_password)
    start_time=perf_counter()
    def brute_password_digits():
        global guesses
        password="".join(rand.choices(digit,k=password_length))
        guesses+=1
        if password==users_password:
            
            end_time=perf_counter()
            elapsed_time=end_time-start_time
            brute_log.config(state="normal")
            brute_log.insert("end", f"\nPassword found. It is {password}\nIt was found in {elapsed_time:.2f} seconds with {guesses} guesses.\n")
            brute_log.see("end")
            brute_log.config(state="disabled")
            guesses=0
        else:
            root.after(1, brute_password_digits)
    brute_password_digits()
def brute_password_special_digits_pre():
    global guesses
    global users_password
    password_length=len(users_password)
    start_time=perf_counter()

    
    def brute_password_special_digits():
        global guesses
        password="".join(rand.choices(special+digit+character,k=password_length))
        guesses+=1
        if password==users_password:
            
            end_time=perf_counter()
            elapsed_time=end_time-start_time
            brute_log.config(state="normal")
            brute_log.insert("end",f"\nPassword found. It is {password}\nIt was found in {elapsed_time:.2f} seconds with {guesses} guesses.\n")
            brute_log.see("end")
            brute_log.config(state="disabled")
            guesses=0
        else:
            root.after(1, brute_password_special_digits)
    brute_password_special_digits()
root=tk.Tk()

root.title("Password Generator and Brute Forcer")

root.geometry("500x600")
root.attributes("-fullscreen", True)
root.configure(bg="black")

title=tk.Label(root, text="Password Generator And Brute Forcer", font=("Arial", 30, "bold"), bg="black", fg="white")
title.pack(anchor="w", padx=20, pady=20)

gen_title=tk.Label(root, text="Password Generator", font=("Arial", 25, "bold"), bg="black", fg="white")
gen_title.pack(anchor="w", padx=20, pady=20)

separator=tk.Frame(root, height=2, bg="white")
separator.pack(fill="x", padx=20, pady=20)

password_label=tk.Label(root, text="Enter password length:", font=("Arial", 20), bg="black", fg="white")
password_label.pack(anchor="w",padx=10, pady=10)

password_length=tk.Entry(root, font=("Arial", 20), bg="black", fg="white", insertbackground="white", insertwidth=2)
password_length.insert(0, " ")
password_length.pack(anchor="w",padx=10, pady=10)

generate_button=tk.Button(root, text="Generate Password", font=("Arial", 20), bg="black", fg="white", command=make_password)
generate_button.pack(anchor="w",padx=10, pady=10)
style=ttk.Style()
checkbox_frame=tk.Frame(root, bg="black")
checkbox_frame.pack(anchor="w", padx=10, pady=10)

special_var=tk.BooleanVar(master=root, value=False)
digit_var=tk.BooleanVar(master=root, value=False)
character_var=tk.BooleanVar(master=root, value=False)

special_characters=tk.Checkbutton(checkbox_frame, text="Special Characters", font=("Arial", 20),                      
                          bg="black", 
                          fg="white", 
                          variable=special_var, 
                          activebackground="black", 
                          selectcolor="black",
                          activeforeground="white")
digits=tk.Checkbutton(checkbox_frame, text="Digits", font=("Arial", 20),
                          bg="black", 
                          fg="white", 
                          variable=digit_var, 
                          activebackground="black", 
                          selectcolor="black",
                          activeforeground="white")
characters=tk.Checkbutton(checkbox_frame, text="Characters", font=("Arial", 20),
                          bg="black", 
                          fg="white", 
                          variable=character_var, 
                          activebackground="black", 
                          selectcolor="black",
                          activeforeground="white")

special_characters.pack(side="left", padx=10, pady=10)
digits.pack(side="left", padx=10, pady=10)
characters.pack(side="left", padx=10, pady=10)


password_frame=tk.Frame(root, bg="black")
password_frame.pack(anchor="w", padx=10, pady=10)

password_label=tk.Label(password_frame, text="Password:", font=("Arial", 20), bg="black", fg="white")
password_label.pack(side="left", padx=10, pady=10)

password_entry=tk.Entry(password_frame, font=("Arial", 20), bg="black", fg="white", state="readonly", readonlybackground="black")
password_entry.pack(side="left",padx=10,pady=10)

copy_password=tk.Button(root, text="Copy Password", font=("Arial", 20), bg="black", fg="white")
copy_password.pack(anchor="w", padx=10, pady=10)
copy_password.config(command=lambda: copy(password_entry.get()))

separator1=tk.Frame(root, height=2, bg="white")
separator1.pack(fill="x", padx=20, pady=20)

brute_title=tk.Label(root, text="Brute Force", font=("Arial", 25, "bold"), bg="black", fg="white")
brute_title.pack(anchor="w", padx=10, pady=10)

seperator2=tk.Frame(root, height=2, bg="white")
seperator2.pack(fill="x", padx=20, pady=20)

brute_password_frame=tk.Frame(root, bg="black")
brute_password_frame.pack(anchor="w", padx=10, pady=10)

brute_label=tk.Label(brute_password_frame, text="Enter the password to brute force:", font=("Arial", 20), bg="black", fg="white")
brute_label.pack(side="left", padx=10, pady=10)

brute_password=tk.Entry(brute_password_frame, font=("Arial", 20), bg="black", fg="white", insertbackground="white", insertwidth=2)
brute_password.pack(side="left", padx=10, pady=10)

brute_command=brute_force

brute_button=tk.Button(root, text="Brute Force", font=("Arial", 20), bg="black", fg="white", command=brute_command)
brute_button.pack(anchor="w", padx=10, pady=10)

brute_bar=ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
brute_bar.pack(anchor="w", padx=10, pady=10)

brute_log=tk.Text(root, font=("Arial", 20), bg="black", fg="white", state="disabled")
brute_log.config(state="normal")
brute_log.insert("end", "v1.0 Brute Forcer\n")
brute_log.config(state="disabled")
brute_log.pack(anchor="w", padx=10, pady=10)

root.mainloop()
