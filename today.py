# to print todays time and date
from datetime import datetime
def print_today():
    today = datetime.now()
    print("Today's date and time:", today.strftime("%Y-%m-%d %H:%M:%S"))
print_today()   