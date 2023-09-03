import tkinter as tk
from time import strftime, localtime

def update_time():
    hours = strftime("%H")
    minutes = strftime("%M")
    seconds = strftime("%S")
    am_or_pm = strftime("%p")
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime('%B %d, %Y')  
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(1000, update_time)  

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=('ds-digital', 40, 'bold'), background='blue', foreground='white')
time_label.pack(anchor='center')


date_label = tk.Label(root, font=('ds-digita', 20), background='blue', foreground='white')
date_label.pack(anchor='nw')


update_time()


root.mainloop()
