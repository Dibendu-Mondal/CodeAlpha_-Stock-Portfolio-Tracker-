stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 3400,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when you are finished entering stocks.\n")


while True:
    stock = input("Enter stock name : ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"✅ Added {quantity} shares of {stock}.\n")

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock} - {qty} shares @ ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("📁 Summary saved to 'portfolio_summary.txt'.")
