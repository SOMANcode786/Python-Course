from datetime import date, datetime

# Get current date
today = date.today()

# Get current time
t = datetime.now().time()

# Print formatted output
print(f"Today's date is: {today} and time is: {t}")
