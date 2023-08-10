def get_input(prompt, data_type, error_message):
    while True:
        user_input = input(prompt)
        try:
            return data_type(user_input)
        except ValueError:
            print(error_message)

h_employee = get_input("How many hours per month do you actually work, including overtime? (e.g. 228): ",
                       int,
                       "Please enter hours as a number (e.g. 228)")

h_employer = get_input("How many hours per month does your employer pay you for? (e.g. 171): ",
                       int,
                       "Please enter hours as a number (e.g. 171)")

r = get_input("How much does your employer pay you for 1 hour? (e.g. 175.0): ",
              float,
              "Please enter rate as a float (e.g. 175.0)")

rate_b = get_input("What is the bonus for 1 hour of overtime? (e.g. 1.5): ",
                   float,
                   "Please enter bonus as a float (e.g. 1.5)")

def computepay(h_employee, h_employer, r, rate_b):
    if h_employee <= h_employer:
        return r * h_employee
    else:
        regular_pay = r * h_employer
        overtime_pay = (h_employee - h_employer) * rate_b * r
        return regular_pay + overtime_pay

total_pay = computepay(h_employee, h_employer, r, rate_b)
print("Total Pay:", total_pay)