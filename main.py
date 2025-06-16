import csv

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 120
}

def get_portfolio():
    """Get stock names and quantities from user input."""
    portfolio = {}
    print("Enter your stocks (type 'done' when finished):")
    
    while True:
        stock = input("Stock symbol (e.g., AAPL): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print(f"Stock {stock} not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            portfolio[stock] = quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    
    return portfolio

def calculate_total_value(portfolio):
    """Calculate total investment value and return details."""
    total_value = 0
    details = []
    
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_value += value
        details.append({
            "Stock": stock,
            "Quantity": quantity,
            "Price": price,
            "Total": value
        })
    
    return total_value, details

def save_to_csv(details, total_value):
    """Save portfolio details to a CSV file."""
    filename = "portfolio_summary.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Stock", "Quantity", "Price", "Total"])
        writer.writeheader()
        writer.writerows(details)
        # Add total value as a separate row
        writer.writerow({"Stock": "TOTAL", "Quantity": "", "Price": "", "Total": total_value})
    print(f"Portfolio saved to {filename}")

def main():
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("-" * 30)
    
    # Get user portfolio
    portfolio = get_portfolio()
    
    if not portfolio:
        print("No stocks entered. Exiting.")
        return
    
    # Calculate and display results
    total_value, details = calculate_total_value(portfolio)
    
    print("\nPortfolio Summary:")
    print("-" * 30)
    for item in details:
        print(f"{item['Stock']}: {item['Quantity']} shares @ ${item['Price']} = ${item['Total']}")
    print("-" * 30)
    print(f"Total Portfolio Value: ${total_value}")
    
    # Ask to save results
    save_choice = input("\nSave results to CSV? (y/n): ").lower()
    if save_choice == 'y':
        save_to_csv(details, total_value)

if __name__ == "__main__":
    main()