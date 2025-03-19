import tkinter as tk
from tkinter import messagebox

def calculate_tip():
    try:
        # Get the values from the entries
        bill_amount = float(entry_bill.get())
        tip_percentage = float(entry_tip.get())
        
        # Calculating the tip and total amount
        tip_amount = (bill_amount * tip_percentage) / 100
        total_amount = bill_amount + tip_amount
        
        # Displaying results
        label_result.config(text=f"Tip: ${tip_amount:.2f}\nTotal: ${total_amount:.2f}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Setting up the main window
root = tk.Tk()
root.title("Tip Calculator")

# Create and place labels and entries for bill and tip percentage
label_bill = tk.Label(root, text="Enter Bill Amount ($):")
label_bill.pack(padx=10, pady=5)

entry_bill = tk.Entry(root)
entry_bill.pack(padx=10, pady=5)

label_tip = tk.Label(root, text="Enter Tip Percentage (%):")
label_tip.pack(padx=10, pady=5)

entry_tip = tk.Entry(root)
entry_tip.pack(padx=10, pady=5)

# Button to calculate tip
calculate_button = tk.Button(root, text="Calculate Tip", command=calculate_tip)
calculate_button.pack(pady=10)

# Label to display the result
label_result = tk.Label(root, text="Tip: $0.00\nTotal: $0.00")
label_result.pack(pady=5)

# Start the GUI event loop
root.mainloop()
