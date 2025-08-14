import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Configure the label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the GUI loop
root.mainloop()
