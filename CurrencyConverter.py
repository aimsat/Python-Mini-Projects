import requests

# Function to get exchange rates from an API (for this example, we'll use an example API URL)
def get_exchange_rates():
    # This is a placeholder URL, replace with an actual API endpoint (e.g., Open Exchange Rates, Fixer.io)
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error if the request failed
        return response.json()['rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

# Function to perform the currency conversion
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Currency code not found: {from_currency} or {to_currency}")
    
    # Convert the amount to the target currency
    conversion_rate = rates[to_currency] / rates[from_currency]
    converted_amount = amount * conversion_rate
    return converted_amount

# Function to validate user input for currency codes
def validate_currency(currency_code, rates):
    if currency_code.upper() not in rates:
        print(f"Invalid currency code: {currency_code}. Please enter a valid currency code.")
        return False
    return True

# Main function to handle user input and display the conversion result
def currency_converter():
    print("Welcome to the Currency Converter!")
    
    # Get the exchange rates
    rates = get_exchange_rates()
    if rates is None:
        print("Unable to fetch exchange rates. Please try again later.")
        return
    
    # Get the amount to convert
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            if amount <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Get the input currency from the user
    while True:
        from_currency = input("Enter the currency code you're converting from (e.g., USD, EUR): ").upper()
        if validate_currency(from_currency, rates):
            break
    
    # Get the output currency from the user
    while True:
        to_currency = input("Enter the currency code you're converting to (e.g., USD, EUR): ").upper()
        if validate_currency(to_currency, rates):
            break
    
    # Perform the conversion
    try:
        result = convert_currency(amount, from_currency, to_currency, rates)
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}.")
    except ValueError as e:
        print(e)

# Start the currency converter
if __name__ == "__main__":
    currency_converter()
