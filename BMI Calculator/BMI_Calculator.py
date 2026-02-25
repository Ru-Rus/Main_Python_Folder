import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def get_activity_multiplier(steps):
    if steps < 5000:
        return "Sedentary", 1.2
    elif steps < 7500:
        return "Light", 1.375
    elif steps < 10000:
        return "Moderate", 1.55
    elif steps < 12500:
        return "Active", 1.725
    else:
        return "Very Active", 1.9


def calculate():
    try:
        gender = gender_var.get()
        age = float(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        steps = int(steps_entry.get())
        weight_unit = weight_unit_var.get()
        height_unit = height_unit_var.get()

        if age <= 0 or weight <= 0 or height <= 0 or steps < 0:
            raise ValueError

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers only.")
        return

    if weight_unit == "lb":
        weight *= 0.453592

    if height_unit == "ft":
        height *= 30.48

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    if bmi <= 16:
        category = "Severely Underweight"
    elif bmi <= 18.5:
        category = "Underweight"
    elif bmi <= 25:
        category = "Healthy"
    elif bmi <= 30:
        category = "Overweight"
    else:
        category = "Severely Overweight"

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_label, multiplier = get_activity_multiplier(steps)
    maintenance = bmr * multiplier

    mild_deficit = maintenance - 300
    aggressive_deficit = maintenance - 500
    target_weight = 22 * (height_m ** 2)

    result = f"""
BMI: {bmi:.2f}
Category: {category}

Steps: {steps} ({activity_label})

Maintenance: {maintenance:.0f} kcal
Mild Fat Loss: {mild_deficit:.0f} kcal
Aggressive Fat Loss: {aggressive_deficit:.0f} kcal

Target Weight (BMI 22): {target_weight:.1f} kg
"""

    result_label.config(text=result)

    with open("bmi_results.txt", "a") as file:
        file.write(f"\nDate: {datetime.now()}\n")
        file.write(result)
        file.write("\n----------------------\n")


# ---------- UI ----------
root = tk.Tk()
root.title("BMI & Calorie Calculator")
root.geometry("600x700")
root.configure(bg="#1e1e2f")

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

title = tk.Label(root,
                 text="BMI & Calorie Calculator",
                 font=("Segoe UI", 20, "bold"),
                 bg="#1e1e2f",
                 fg="white")
title.grid(row=0, column=0, pady=20)

main_frame = tk.Frame(root, bg="#2a2a40", padx=30, pady=30)
main_frame.grid(row=1, column=0, sticky="nsew", padx=30, pady=10)

main_frame.columnconfigure(0, weight=1)


def styled_label(text):
    return tk.Label(main_frame,
                    text=text,
                    bg="#2a2a40",
                    fg="white",
                    font=("Segoe UI", 11))


def styled_entry():
    return tk.Entry(main_frame,
                    font=("Segoe UI", 11),
                    bg="#3a3a55",
                    fg="white",
                    insertbackground="white",
                    relief="flat")


row = 0

styled_label("Gender").grid(row=row, column=0, sticky="w")
row += 1
gender_var = tk.StringVar(value="Male")
tk.OptionMenu(main_frame, gender_var, "Male", "Female").grid(row=row, column=0, sticky="ew", pady=5)
row += 1

styled_label("Age").grid(row=row, column=0, sticky="w")
row += 1
age_entry = styled_entry()
age_entry.grid(row=row, column=0, sticky="ew", pady=5)
row += 1

styled_label("Weight").grid(row=row, column=0, sticky="w")
row += 1
weight_entry = styled_entry()
weight_entry.grid(row=row, column=0, sticky="ew", pady=5)
row += 1

weight_unit_var = tk.StringVar(value="kg")
tk.OptionMenu(main_frame, weight_unit_var, "kg", "lb").grid(row=row, column=0, sticky="ew", pady=5)
row += 1

styled_label("Height").grid(row=row, column=0, sticky="w")
row += 1
height_entry = styled_entry()
height_entry.grid(row=row, column=0, sticky="ew", pady=5)
row += 1

height_unit_var = tk.StringVar(value="cm")
tk.OptionMenu(main_frame, height_unit_var, "cm", "ft").grid(row=row, column=0, sticky="ew", pady=5)
row += 1

styled_label("Daily Step Count").grid(row=row, column=0, sticky="w")
row += 1
steps_entry = styled_entry()
steps_entry.grid(row=row, column=0, sticky="ew", pady=5)
row += 1

tk.Button(main_frame,
          text="Calculate",
          command=calculate,
          bg="#4CAF50",
          fg="white",
          font=("Segoe UI", 12, "bold"),
          relief="flat",
          pady=12).grid(row=row, column=0, sticky="ew", pady=20)

result_label = tk.Label(root,
                        text="",
                        bg="#1e1e2f",
                        fg="#00ffcc",
                        font=("Consolas", 12),
                        justify="left")
result_label.grid(row=2, column=0, pady=20)

root.mainloop()