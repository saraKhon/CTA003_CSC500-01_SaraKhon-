"""
Student: Saravenus Khon, Date: 04/08/2025, CTA03 - Creating Python Programs
"""

# Part 01

#  defined function
def total_meals_purchased():
    # collect user input
    Meal_cost= float(input("Please enter the meal cost here:$"))

    #add the tip (18%) and tax(7%)
    tip = Meal_cost * 0.18
    tax = Meal_cost * 0.07
    total_Meal_cost = Meal_cost + tip + tax

    # Shows the output for the input, tip, tax and total meal cost
    print("\t ---- Meal Receipt ---")
    print(f"Meal Charge ..............${Meal_cost:.2f}")
    print(f"+ 18% manual gratuity..... ${tip:.2f}")
    print(f"+ 7% sales tax.............${tax:.2f}")
    print(f"\nYour Total Meal Cost is...${total_Meal_cost:.2f}")

#run the functon
total_meals_purchased()

print("\n ----------------------------------------------------------------------")

#Part II:

def AlarmTime_Calculation():
    # ask the user for the current time in 24hr format
    current_time = int(input("Enter the current Military Time (0 hr to 23 hr): "))

    # Ask the user to input the amount of hours to wait for the alam
    hours_to_wait = int(input("Now, enter how many hours you want to wait: "))

    #process the calculations for the alarm to ring /24hrs
    alarm = (current_time+hours_to_wait) % 24

    #print out the results
    print(f"Your alarm will go off at {alarm}:00 on a 24 hr clock.")


#run the function
AlarmTime_Calculation()




