"""
This program calculates the total bill amount, tip amount, and optionally splits the bill among multiple people.
"""


def calculate_tip(bill_amount, tip_percentage):
    tip = (bill_amount * tip_percentage) / 100
    rounded_tip = round(tip, 2)
    return rounded_tip


def calculate_total_bill(bill_amount, tip_amount):
    total_amount = bill_amount + tip_amount
    return total_amount


def split_bill(total_amount, num_people):
    split_amount = total_amount / num_people
    rounded_split_amount = round(split_amount, 2)
    return rounded_split_amount


def calculate_bill():
    bill_amount = float(input("Bill amount: "))
    tip_percentage = float(input("Tip percentage (%): "))

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_amount = calculate_total_bill(bill_amount, tip_amount)

    print("Your bill total:", bill_amount)
    print("Your tip total:", tip_amount)

    while True:
        cut_the_check = input("Would you like to split the bill? (y/n) ")
        if cut_the_check == "n":
            print("The final amount:", total_amount)
            break
        elif cut_the_check == "y":
            split = int(input("Split the bill between how many people? "))
            split_bill_amount = split_bill(total_amount, split)
            print("Each person's individual total is:", split_bill_amount)
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


calculate_bill()
