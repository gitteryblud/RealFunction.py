# Function 1: Circle Function
def circle_area(radius: float) -> float:
    pi = 3.14159
    area = pi * (radius ** 2)
    return area


# Function 2: Taxes Function
def calculate_total_due(money: float, tax_rate: float) -> float:
    total_due = money + (money * tax_rate)
    return total_due


# Function 3: Temperature Function
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


# --- Test Executions ---

print("===Circle Area Tests===")
circle_inputs = [10, 6, 24, 2, 1]
for r in circle_inputs:
    result = circle_area(r)
    # Formatted to match test output examples
    print(f"Radius: {r} -> Area: {result:.2f}")

print("\n=== Taxes Tests ===")
tax_tests = [
    (20, 0.06),  # 6%
    (54, 0.04),  # 4%
    (68, 0.08),  # 8%
]
for amount, rate in tax_tests:
    total = calculate_total_due(amount, rate)
    print(f"Money: ${amount}, Tax: {int(rate * 100)}% -> Total: {total:.2f}")

print("\n=== Temperature Tests ===")
temp_inputs = [32, 80, 73, 42]
for f in temp_inputs:
    c = fahrenheit_to_celsius(f)
    print(f"Fahrenheit: {f}°F -> Celsius: {c:.4f}°C")