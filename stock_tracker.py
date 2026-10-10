STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    portfolio = {}

    print("Available stocks:", ", ".join(STOCK_PRICES))
    print("Type 'done' as the stock name when you are finished.\n")

    while True:
        name = input("Enter stock name: ").strip().upper()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print(f"  '{name}' is not in our price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {name}: "))
        except ValueError:
            print("  Please enter a whole number.\n")
            continue

        if quantity <= 0:
            print("  Quantity must be greater than 0.\n")
            continue

        portfolio[name] = portfolio.get(name, 0) + quantity
        print(f"  Added {quantity} x {name}\n")

    return portfolio


def calculate_total(portfolio):
    lines = []
    total = 0

    for name, quantity in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * quantity
        total += value
        lines.append((name, quantity, price, value))

    return lines, total


def build_report(lines, total):
    report = ["=" * 48, "STOCK PORTFOLIO SUMMARY".center(48), "=" * 48]
    report.append(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}")
    report.append("-" * 48)

    for name, quantity, price, value in lines:
        report.append(f"{name:<8}{quantity:>6}{'$' + str(price):>10}{'$' + format(value, ','):>14}")

    report.append("-" * 48)
    report.append(f"{'TOTAL INVESTMENT:':<24}{'$' + format(total, ','):>24}")
    report.append("=" * 48)
    return "\n".join(report)


def save_to_file(report, filename="portfolio_result.txt"):
    with open(filename, "w") as file:
        file.write(report)
    print(f"\nResult saved to '{filename}'")


def main():
    print("--- Stock Portfolio Tracker ---\n")

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    lines, total = calculate_total(portfolio)
    report = build_report(lines, total)
    print("\n" + report)

    choice = input("\nSave this result to a file? (yes/no): ").strip().lower()
    if choice in ("yes", "y"):
        save_to_file(report)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
