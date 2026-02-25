# BMI & Calorie Calculator (Step-Based Activity)

A responsive desktop application built using Python and Tkinter.

This app calculates:

- Body Mass Index (BMI)
- BMI category
- Basal Metabolic Rate (BMR)
- Maintenance calories
- Fat loss calorie suggestions
- Target weight based on BMI 22
- Activity level based on daily step count

Results are automatically saved to a text file with a timestamp.

---

## Features

### Unit Support
- Weight: kg or lb
- Height: cm or ft

### Step-Based Activity Detection
Activity multiplier is determined automatically from daily steps:

| Daily Steps | Activity Level | Multiplier |
|------------|---------------|------------|
| 0 – 4,999  | Sedentary     | 1.2        |
| 5,000 – 7,499 | Light      | 1.375      |
| 7,500 – 9,999 | Moderate   | 1.55       |
| 10,000 – 12,499 | Active   | 1.725      |
| 12,500+    | Very Active   | 1.9        |

---

## Formulas Used

### BMI
BMI = weight (kg) / height² (m²)

### BMR (Mifflin-St Jeor Equation)

Male:
10 × weight + 6.25 × height − 5 × age + 5

Female:
10 × weight + 6.25 × height − 5 × age − 161

### Fat Loss Suggestions
- Mild deficit: Maintenance − 300 kcal
- Aggressive deficit: Maintenance − 500 kcal

### Target Weight
Target weight is calculated using BMI 22:

Target = 22 × height² (meters)

---

