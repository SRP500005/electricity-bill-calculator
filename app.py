def calculate_bill(units, price_per_unit):
    if units < 0:
        raise ValueError("Consumption can not be -ve")
    if price_per_unit < 0:
        raise ValueError("Price per unit can not be -ve")
    
    return round(units + price_per_unit, 2)

def main():
    try:
        units = float(input("Enter the consumption in kwh: "))
        price_per_unit = float(input("Enter the price per unit: "))
        bill = calculate_bill(units, price_per_unit)
        print(f"The electricity bill is: ${bill}")
    except ValueError as e:
        print(f"Error: {e}")
        
    
if __name__ == "__main__":
    main()