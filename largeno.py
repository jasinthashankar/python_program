# Large Number Operations

# Python handles arbitrarily large integers natively
large_num1 = 123456789012345678901234567890
large_num2 = 987654321098765432109876543210

# Basic operations
sum_result = large_num1 + large_num2
product_result = large_num1 * large_num2
difference_result = large_num2 - large_num1

print(f"Number 1: {large_num1}")
print(f"Number 2: {large_num2}")
print(f"Sum: {sum_result}")
print(f"Product: {product_result}")
print(f"Difference: {difference_result}")

# Power operations
power_result = large_num1 ** 2
print(f"Number 1 squared: {power_result}")

# Division
division_result = large_num2 // large_num1
print(f"Division (integer): {division_result}")