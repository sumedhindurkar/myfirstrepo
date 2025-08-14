import tkinter as tk
from tkinter import messagebox
from time import strftime

# Global variable to store alarm time
alarm_set_time = None

def update_time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)
    check_alarm(current_time)

def set_alarm():
    global alarm_set_time
    alarm_time = f"{hour_var.get()}:{minute_var.get()}:{second_var.get()} {ampm_var.get()}"
    alarm_label.config(text=f"Alarm set for: {alarm_time}")
    alarm_set_time = alarm_time

def check_alarm(current_time):
    global alarm_set_time
    if alarm_set_time and current_time == alarm_set_time:
        messagebox.showinfo("Alarm", "Time's up!")
        alarm_set_time = None  # Reset alarm

# GUI setup
root = tk.Tk()
root.title("Digital Clock with Alarm")

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
clock_label.pack(pady=20)

alarm_frame = tk.Frame(root)
alarm_frame.pack(pady=10)

tk.Label(alarm_frame, text="Set Alarm Time (HH:MM:SS AM/PM):").grid(row=0, column=0, columnspan=4)

hour_var = tk.StringVar(value='07')
minute_var = tk.StringVar(value='00')
second_var = tk.StringVar(value='00')
ampm_var = tk.StringVar(value='AM')

tk.Entry(alarm_frame, textvariable=hour_var, width=3).grid(row=1, column=0)
tk.Entry(alarm_frame, textvariable=minute_var, width=3).grid(row=1, column=1)
tk.Entry(alarm_frame, textvariable=second_var, width=3).grid(row=1, column=2)
tk.OptionMenu(alarm_frame, ampm_var, 'AM', 'PM').grid(row=1, column=3)

tk.Button(alarm_frame, text="Set Alarm", command=set_alarm).grid(row=2, column=0, columnspan=4, pady=5)

alarm_label = tk.Label(root, text="", font=('calibri', 12))
alarm_label.pack()

update_time()
root.mainloop()
