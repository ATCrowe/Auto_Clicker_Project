import tkinter as tk
from tkinter import ttk

def log_key(event):
    global start_hotkey, stop_hotkey
    if start_hotkey_entry.state():
        start_hotkey_entry.delete(0, tk.END)
        start_hotkey_entry.insert(0, event.keysym)
        return "break"  # Prevents key from being inserted twice
    elif stop_hotkey_entry.state():
        stop_hotkey_entry.delete(0, tk.END)
        stop_hotkey_entry.insert(0, event.keysym)
        return "break"  # Prevents key from being inserted twice

def reset_values():
    mins_entry.delete(0, tk.END)
    mins_entry.insert(0, "0")
    secs_entry.delete(0, tk.END)
    secs_entry.insert(0, "0")
    ms_entry.delete(0, tk.END)
    ms_entry.insert(0, "0")
    click_dropdown.set("Right")
    start_hotkey_entry.delete(0, tk.END)
    stop_hotkey_entry.delete(0, tk.END)
    until_stopped_radio.select()
    hold_button_var.set(0)
    repeat_entry.delete(0, tk.END)
    repeat_entry.insert(0, "1")

root = tk.Tk()
root.title("AutoClicker")
root.geometry("350x460")  # Set the initial size of the window
root.resizable(False, False)  # Make the window fixed size

icon = tk.PhotoImage(file='mouselogo.png')
root.iconphoto(True, icon)

# Set Interval
interval_frame = ttk.LabelFrame(root, text="Set Interval")
interval_frame.pack(padx=10, pady=10)

mins_label = ttk.Label(interval_frame, text="Mins:")
mins_label.grid(row=0, column=0, padx=5, pady=5)
mins_entry = ttk.Entry(interval_frame, width=5)
mins_entry.grid(row=0, column=1, padx=5, pady=5)
mins_entry.insert(0, "0")

secs_label = ttk.Label(interval_frame, text="Secs:")
secs_label.grid(row=0, column=2, padx=5, pady=5)
secs_entry = ttk.Entry(interval_frame, width=5)
secs_entry.grid(row=0, column=3, padx=5, pady=5)
secs_entry.insert(0, "0")

ms_label = ttk.Label(interval_frame, text="Milliseconds:")
ms_label.grid(row=0, column=4, padx=5, pady=5)
ms_entry = ttk.Entry(interval_frame, width=5)
ms_entry.grid(row=0, column=5, padx=5, pady=5)
ms_entry.insert(0, "0")

# Click Direction
click_frame = ttk.LabelFrame(root, text="Click Direction")
click_frame.pack(padx=10, pady=10)

click_var = tk.StringVar(value="Right")
click_dropdown = ttk.Combobox(click_frame, textvariable=click_var, values=["Right", "Left"])
click_dropdown.grid(row=0, column=0, padx=5, pady=5)

# Start Hotkey
start_hotkey_frame = ttk.LabelFrame(root, text="Start Hotkey")
start_hotkey_frame.pack(padx=10, pady=10)

start_hotkey_entry = ttk.Entry(start_hotkey_frame, width=20)
start_hotkey_entry.grid(row=0, column=0, padx=5, pady=5)
start_hotkey_entry.bind("<KeyPress>", log_key)

# Stop Hotkey
stop_hotkey_frame = ttk.LabelFrame(root, text="Stop Hotkey")
stop_hotkey_frame.pack(padx=10, pady=10)

stop_hotkey_entry = ttk.Entry(stop_hotkey_frame, width=20)
stop_hotkey_entry.grid(row=0, column=0, padx=5, pady=5)
stop_hotkey_entry.bind("<KeyPress>", log_key)

# Radio Buttons and Hold Button
radio_frame = ttk.LabelFrame(root, text="Options")
radio_frame.pack(padx=10, pady=10)

option_var = tk.StringVar(value="Until Stopped")
until_stopped_radio = ttk.Radiobutton(radio_frame, text="Until Stopped", variable=option_var, value="Until Stopped")
until_stopped_radio.grid(row=0, column=0, padx=5, pady=5)

repeat_radio = ttk.Radiobutton(radio_frame, text="Repeat", variable=option_var, value="Repeat")
repeat_radio.grid(row=0, column=1, padx=5, pady=5)

hold_button_var = tk.IntVar(value=0)
hold_button_check = ttk.Checkbutton(radio_frame, text="Hold Button", variable=hold_button_var)
hold_button_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Defaulted at 1
repeat_label = ttk.Label(radio_frame, text="Repeat Count:")
repeat_label.grid(row=2, column=0, padx=5, pady=5)
repeat_entry = ttk.Entry(radio_frame, width=5)
repeat_entry.grid(row=2, column=1, padx=5, pady=5)
repeat_entry.insert(0, "1")

# Reset Button
reset_button = ttk.Button(root, text="Reset", command=reset_values)
reset_button.pack(pady=10)

root.mainloop()

