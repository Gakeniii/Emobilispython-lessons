# Create a program that takes 2 user inputs ie height and weight.
# The height and weight can be either interger or float numbers
# Then calculate the BMI of that individual from the inputs keyed in by the user
#ensure you display the Body Mass Index=Weight(kg)/height*(Meters
# the BMI into 4 categories that is underweight which is at the range of
# less than 18, normal which is at the range of 18-24 over-weight which is
# at the range of 25-30 and lastly abnormally overweight past 30

weight = float(input("What is your weight in kilograms? "))
height = float(input("What is your height in meters? "))
BMI = (weight/height)
print(f"Your BMI is {BMI}")
if BMI >=1 and  BMI <=18:
    print("You are severely underweight, please consult a doctor")
elif BMI >= 18.5 and BMI <=24:
    print("You are in the normal weight category. Congratulations!")
elif BMI >=25 and BMI <=30:
    print("You are overweight please lose weight :)")
elif BMI >=30 and BMI <=50:
    print("You are abnormally obese. STOP EATING!!!")
else:
    print("Invalid input")

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight_kg / (height_m ** 2)

def main():
    # Get user input for weight and height
    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Display the result
    print("Your BMI is:", bmi)

if __name__ == "__main__":
    main()


