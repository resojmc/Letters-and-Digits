import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Letters and Digits")

def count_digits(s):
    count = 0
    for char in s:
        if char.isdigit():
            count = count + 1

    return count

def count_letters(s):
    count = 0
    for char in s:
        if char.isalpha():
            count = count + 1

    return count
    
def update_st():
    string = top_entry.get()
    digits = count_digits(string)
    letters = count_letters(string)
    bottom_label.config(text=f""" Results for -{string}- :
    Digits: {digits}
    Letters: {letters}
    """)
    
top_label = tk.Label(root, text="Returns amount of letters and Digits.")
top_label.pack()

top_entry = tk.Entry(root, )
top_entry.pack()

button = tk.Button(root, text="Go", command=update_st)
button.pack()

bottom_label = tk.Label(root, text="Results: ")
bottom_label.pack()

root.mainloop()