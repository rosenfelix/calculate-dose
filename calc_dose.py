from datetime import datetime, timedelta

# A program that helps you calculate how long a prescription will last.
# You enter information about the prescription (start date, total number of doses, maximal daily dose).
# The program then gives you an answer of how many days the medication will last and how many doses will be left over.

def calc_dose(date, total_dose, daily_dose):
    number_of_dose_days = int(total_dose / daily_dose)
    dose_days = timedelta((total_dose / daily_dose) - 1)

    # Calculate the last full dose day
    last_dose_day = date + dose_days
    last_dose_day = str(last_dose_day)[:10]

    # Calculate the remaining doses after the last full dose day
    remaining_doses = total_dose % daily_dose

    # Output
    if remaining_doses % 1 == 0.0:
        remaining_doses = int(remaining_doses)
    print(f'\nThe medication can be taken as prescribed for {number_of_dose_days} full days, until {last_dose_day}.\nAfter {last_dose_day}, there are {remaining_doses} doses remaining.')

print('---WISEMED / FELIX ROSÉN---')

# User input - prescription start date
while True:
    date = input("When should the first dose be taken? (YYYYMMDD)\n")
    try:
        date = datetime.strptime(date, "%Y%m%d")
        break
    except:
        print(f"Invalid date. Try again.")
        continue

# User input - number of doses in the prescription
while True:
    total_dose = input("How many doses are in the prescription?\n")
    try:
        total_dose = float(total_dose)
        break
    except:
        print(f"Invalid number of doses. Try again.\nNOTE! Use a decimal point if needed, e.g., 1.5.")
        continue

# User input - maximum daily dose
while True:
    daily_dose = input("What is the maximum daily dose?\n")
    try:
        daily_dose = float(daily_dose)
        break
    except:
        print(f"Invalid dose amount. Try again.\nNOTE! Use a decimal point if needed, e.g., 1.5.")
        continue

calc_dose(date, total_dose, daily_dose)

print('---WISEMED / FELIX ROSÉN---')
