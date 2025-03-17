import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and set the main content frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.grid(column=0, row=0)

# Create the Fahrenheit entry frame with label and entry
frm_entry = tk.Frame(main_frame)
frm_entry.pack(side="left", padx=10)

lbl_temperature = tk.Label(frm_entry, text="Fahrenheit:")
lbl_temperature.pack(side="left")

ent_temperature = tk.Entry(frm_entry)
ent_temperature.pack(side="left")

# Create the conversion button and result display label
btn_convert = tk.Button(main_frame, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
btn_convert.pack(side="left", padx=10)

lbl_result = tk.Label(main_frame, text="\N{DEGREE CELSIUS}")
lbl_result.pack(side="left")

# Start the GUI event loop
root.mainloop()
