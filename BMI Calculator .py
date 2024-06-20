
print("Welcome to BMI Calculator")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    if weight <= 0 or height <= 0:
        print("Weight and height must be positive values.")
    else:
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")

except ValueError:
    print("Please enter valid numbers for weight and height.")
