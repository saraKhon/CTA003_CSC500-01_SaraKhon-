from cherrypy.tutorial.tut02_expose_methods import HelloWorld

print(HelloWorld)


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



#Part II:
