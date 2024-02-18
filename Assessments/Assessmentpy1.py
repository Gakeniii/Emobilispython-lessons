# write a program that accepts 1 to 12
# and displays the name of the month,
# that is from January to December
# like when the user types 1 it displays January

def display_month_name(month_number):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        month_name = months[month_number - 1]
        print(f" The month is {month_name}!")
    else:
        print("Invalid input for month number.")


# Accept user input
month_number = int(input("Enter a number between 1 and 12: "))

display_month_name(month_number)





















