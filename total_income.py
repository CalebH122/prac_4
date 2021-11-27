def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input(f"Enter income for month {total_months}: "))
        incomes.append(income)

    income_report(incomes, total_months)


def income_report(incomes, total_months):
    """This function will collect all the income data, and then print out the report for us"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
