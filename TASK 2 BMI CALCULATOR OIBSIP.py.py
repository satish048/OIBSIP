import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())

        if weight <= 0 or height_cm <= 0:
            raise ValueError

        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        category = get_bmi_category(bmi)

        result_var.set(f"BMI: {bmi:.2f} ({category})")
        save_to_file(weight, height_cm, bmi, category)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid positive numbers for weight and height.")

# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to save data to a CSV file
def save_to_file(weight, height_cm, bmi, category):
    with open("bmi_data.csv", "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{date},{weight},{height_cm},{bmi:.2f},{category}\n")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.resizable(False, False)

# Weight input
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1)

# Height input (in centimeters)
tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, columnspan=2, pady=10)

# Result display
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 12), fg="blue").grid(row=3, columnspan=2, pady=5)

root.mainloop()
