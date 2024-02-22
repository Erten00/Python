def add_debt(name, debt, debts_dict):
    """
    Add a debt for a person to the debts dictionary.
    """
    debts_dict[name] = debt


def main():
    debts = {}  # Dictionary to store debts

    while True:
        print("\n1. Add Debt\n2. View Debts\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter the name of the person: ")
            debt = float(input("Enter the debt amount: "))
            add_debt(name, debt, debts)
            print("Debt added successfully!")

        elif choice == '2':
            print("\nDebts:")
            if debts:
                for name, debt in debts.items():
                    print(f"{name}: ${debt}")
            else:
                print("No debts recorded yet.")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
