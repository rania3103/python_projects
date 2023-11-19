#!/usr/bin/python3
"""tracking phone number"""

# we have to install phone numbers unsing pip install phonenumbers
from phonenumbers import geocoder, carrier, timezone, parse

print("-" * 70)

enter_phonenumber = input("Enter please the phone number with country code: ")

# create phone number object
phone_numb = parse(enter_phonenumber, None)
print(phone_numb)

"""
if we want to specify a country for example Tunisia
phone_numb = parse(enter_phonenumber, "TN")
and we enter a phone number in the input without the country code
"""

# get the location that corresponds to the phone number and
print(geocoder.country_name_for_number(phone_numb, "en"))
"""
we can chose in which lang the output will be for french just replace
"en" with "fr"
"""

# get the carrier that owns the phone number
print(carrier.name_for_number(phone_numb, "en"))

# get list of tme zones associated with the phone number
print(timezone.time_zones_for_number(phone_numb))
