# to print todays time and date
from datetime import datetime
def print_today():
    today = datetime.now()
    print("Today's date and time:", today.strftime("%Y-%m-%d %H:%M:%S"))
print_today()

# error handling in python
try:
    # Example: dividing by zero to raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Error handling complete.")

# example of error handling when reading a file
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print("Error: The file was not found.")
except Exception as e:
    print("An unexpected error occurred while reading the file:", e)
finally:
    print("File handling complete.")   