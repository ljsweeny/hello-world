"""Simple financial budgeting calculator."""

def calculate_budget(income, expenses):
    """Return remaining budget after subtracting expenses from income.

    Parameters
    ----------
    income : float
        Total income amount.
    expenses : list[float]
        List of expense amounts.

    Returns
    -------
    float
        Remaining budget.
    """
    return income - sum(expenses)


def main():
    print("Simple Budget Calculator")
    income = float(input("Enter your total income: "))
    expenses = []
    print("Enter your expenses one by one. Type 'done' when finished:")
    while True:
        entry = input("Expense amount: ")
        if entry.lower() == 'done':
            break
        try:
            expenses.append(float(entry))
        except ValueError:
            print("Please enter a valid number or 'done'.")
    remaining = calculate_budget(income, expenses)
    print(f"Remaining budget: ${remaining:.2f}")


if __name__ == "__main__":
    main()
