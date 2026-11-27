import secrets 
from time import perf_counter
import string
import random as rand
import tkinter as tk
from tkinter import messagebox as msg, filedialog as fd, ttk
from pyperclip import copy
import subprocess
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
    global users_password, guesses
    users_password=brute_password.get()
    if not users_password:
        msg.showerror("Error", "Please enter a password to brute force")
        return
    guesses = 0
    brute_bar["value"] = 0
    brute_pct_label.config(text="Estimated progress: 0%")
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
    charset = character + special
    total = len(charset) ** password_length
    def brute_password_with_special():
        global guesses
        password="".join(rand.choices(charset,k=password_length))
        guesses+=1
        pct = min((guesses / total) * 100, 100)
        brute_bar["value"] = pct
        brute_pct_label.config(text=f"Estimated progress: {pct:.4f}%")
        if password==users_password:
            brute_bar["value"] = 100
            brute_pct_label.config(text="Estimated progress: 100%")
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
    charset = character
    total = len(charset) ** password_length
    def brute_password_normal():
        global guesses
        password="".join(rand.choices(charset,k=password_length))
        guesses+=1
        pct = min((guesses / total) * 100, 100)
        brute_bar["value"] = pct
        brute_pct_label.config(text=f"Estimated progress: {pct:.4f}%")
        if password==users_password:
            brute_bar["value"] = 100
            brute_pct_label.config(text="Estimated progress: 100%")
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
    charset = digit
    total = len(charset) ** password_length
    def brute_password_digits():
        global guesses
        password="".join(rand.choices(charset,k=password_length))
        guesses+=1
        pct = min((guesses / total) * 100, 100)
        brute_bar["value"] = pct
        brute_pct_label.config(text=f"Estimated progress: {pct:.4f}%")
        if password==users_password:
            brute_bar["value"] = 100
            brute_pct_label.config(text="Estimated progress: 100%")
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
    charset = special + digit + character
    total = len(charset) ** password_length
    def brute_password_special_digits():
        global guesses
        password="".join(rand.choices(charset,k=password_length))
        guesses+=1
        pct = min((guesses / total) * 100, 100)
        brute_bar["value"] = pct
        brute_pct_label.config(text=f"Estimated progress: {pct:.4f}%")
        if password==users_password:
            brute_bar["value"] = 100
            brute_pct_label.config(text="Estimated progress: 100%")
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

page_canvas=tk.Canvas(root, bg="black", highlightthickness=0)
page_scrollbar=tk.Scrollbar(root, orient="vertical", command=page_canvas.yview)
page_canvas.configure(yscrollcommand=page_scrollbar.set)

page_scrollbar.pack(side="right", fill="y")
page_canvas.pack(side="left", fill="both", expand=True)

content_frame=tk.Frame(page_canvas, bg="black")
page_window=page_canvas.create_window((0, 0), window=content_frame, anchor="nw")

def _on_content_configure(event):
    page_canvas.configure(scrollregion=page_canvas.bbox("all"))

def _on_canvas_configure(event):
    page_canvas.itemconfig(page_window, width=event.width)

content_frame.bind("<Configure>", _on_content_configure)
page_canvas.bind("<Configure>", _on_canvas_configure)

def _page_mousewheel(event):
    w = event.widget
    try:
        if w == brute_log or w == brute_log_scroll or str(w).startswith(str(brute_log_frame)):
            return
    except Exception:
        pass
    page_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root.bind_all("<MouseWheel>", _page_mousewheel)

title=tk.Label(content_frame, text="Password Generator And Brute Forcer", font=("Arial", 30, "bold"), bg="black", fg="white")
title.pack(anchor="w", padx=20, pady=20)

logo=tk.PhotoImage(file="Lock(WHITE).png")
logo=logo.zoom(3,3)
logo_label=tk.Label(root, image=logo, bg="black")
logo_label.place(relx=1.0,x=-20,y=10, anchor="ne")

gen_title=tk.Label(content_frame, text="Password Generator", font=("Arial", 25, "bold"), bg="black", fg="white")
gen_title.pack(anchor="w", padx=20, pady=20)

separator=tk.Frame(content_frame, height=2, bg="white")
separator.pack(fill="x", padx=20, pady=20)

password_label=tk.Label(content_frame, text="Enter password length:", font=("Arial", 20), bg="black", fg="white")
password_label.pack(anchor="w",padx=10, pady=10)

password_length=tk.Entry(content_frame, font=("Arial", 20), bg="black", fg="white", insertbackground="white", insertwidth=2)
password_length.insert(0, " ")
password_length.pack(anchor="w",padx=10, pady=10)

generate_button=tk.Button(content_frame, text="Generate Password", font=("Arial", 20), bg="black", fg="white", command=make_password)
generate_button.pack(anchor="w",padx=10, pady=10)
style=ttk.Style()
checkbox_frame=tk.Frame(content_frame, bg="black")
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


password_frame=tk.Frame(content_frame, bg="black")
password_frame.pack(anchor="w", padx=10, pady=10)

password_label=tk.Label(password_frame, text="Password:", font=("Arial", 20), bg="black", fg="white")
password_label.pack(side="left", padx=10, pady=10)

password_entry=tk.Entry(password_frame, font=("Arial", 20), bg="black", fg="white", state="readonly", readonlybackground="black")
password_entry.pack(side="left",padx=10,pady=10)

copy_password=tk.Button(content_frame, text="Copy Password", font=("Arial", 20), bg="black", fg="white")
copy_password.pack(anchor="w", padx=10, pady=10)
copy_password.config(command=lambda: copy(password_entry.get()))

separator1=tk.Frame(content_frame, height=2, bg="white")
separator1.pack(fill="x", padx=20, pady=20)

brute_title=tk.Label(content_frame, text="Brute Force", font=("Arial", 25, "bold"), bg="black", fg="white")
brute_title.pack(anchor="w", padx=10, pady=10)

seperator2=tk.Frame(content_frame, height=2, bg="white")
seperator2.pack(fill="x", padx=20, pady=20)

brute_password_frame=tk.Frame(content_frame, bg="black")
brute_password_frame.pack(anchor="w", padx=10, pady=10)

brute_label=tk.Label(brute_password_frame, text="Enter the password to brute force:", font=("Arial", 20), bg="black", fg="white")
brute_label.pack(side="left", padx=10, pady=10)

brute_password=tk.Entry(brute_password_frame, font=("Arial", 20), bg="black", fg="white", insertbackground="white", insertwidth=2)
brute_password.pack(side="left", padx=10, pady=10)

brute_command=brute_force

brute_button=tk.Button(content_frame, text="Brute Force", font=("Arial", 20), bg="black", fg="white", command=brute_command)
brute_button.pack(anchor="w", padx=10, pady=10)

brute_bar=ttk.Progressbar(content_frame, orient="horizontal", mode="determinate", maximum=100)
brute_bar.pack(anchor="w", fill="x", padx=10, pady=10)

brute_pct_label=tk.Label(content_frame, text="Estimated progress: 0%", font=("Arial", 14), bg="black", fg="white")
brute_pct_label.pack(anchor="w", padx=10, pady=(0, 10))


brute_log_frame=tk.Frame(content_frame, bg="black")
brute_log_frame.pack(anchor="w", fill="both", expand=True, padx=10, pady=10)

brute_log_scroll=tk.Scrollbar(brute_log_frame, orient="vertical")
brute_log_scroll.pack(side="right", fill="y")

brute_log=tk.Text(brute_log_frame, font=("Arial", 20), bg="black", fg="white", state="disabled", height=20, wrap="word", yscrollcommand=brute_log_scroll.set)
brute_log.config(state="normal")
brute_log.insert("end", "v1.0 Brute Forcer\n")
brute_log.config(state="disabled")
brute_log.pack(side="left", fill="both", expand=True)

brute_log_scroll.config(command=brute_log.yview)

def _brute_log_mousewheel(event):
    brute_log.yview_scroll(int(-1 * (event.delta / 120)), "units")
    return "break"

brute_log.bind("<MouseWheel>", _brute_log_mousewheel)
brute_log.bind("<Button-4>", lambda e: (brute_log.yview_scroll(-1, "units"), "break"))
brute_log.bind("<Button-5>", lambda e: (brute_log.yview_scroll(1, "units"), "break"))
brute_log_frame.bind("<MouseWheel>", _brute_log_mousewheel)
brute_log.bind("<Enter>", lambda e: brute_log.focus_set())

root.mainloop()
