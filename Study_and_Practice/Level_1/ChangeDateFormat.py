# Program to convert dates from yyyy-mm-dd to dd-mm-yyyy

from _datetime import datetime


def convert_date(date_str):
    try:
        # convert string to datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        # format datetime object as dd-mm-yyyy
        formatted_date = date_obj.strftime('%d-%m-%Y')
        return formatted_date
    except ValueError:
        return "Invalid date format. Please enter it in yyyy-mm-dd format."


# Test the function
date_input = input("Enter a date in yyyy-mm-dd format: ")
converted_date = convert_date(date_input)
print("Converted date: ", converted_date)
