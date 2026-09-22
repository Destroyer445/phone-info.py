# Phone Info Tool - By DESTROYER445
import phonenumbers
from phonenumbers import carrier, geocoder
number = input("Enter number with +91: ")
parsed = phonenumbers.parse(number, None)
print(f"Region: {geocoder.description_for_number(parsed, 'en')}")
print(f"Carrier: {carrier.name_for_number(parsed, 'en')}")
print(f"Valid: {phonenumbers.is_valid_number(parsed)}")
