from datetime import datetime

def calculate_age():
    
    dob_input = input("Enter your date of birth (DD-MM-YYY): ")
    
    try:
        dob_date = datetime.strptime(dob_input, '%d-%m-%Y')

        today = datetime.today()

        age = today.year - dob_date.year
        
        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1
        
        return age
    
    except ValueError:
        return "Invalid date format"

age = calculate_age()
print(f"Your age is: {age}")
