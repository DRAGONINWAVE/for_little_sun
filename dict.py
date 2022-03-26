import items as items

dial_codes = [(880,'Bangladesh'),(55,'Brazil'),(86,'China'),(91,'India'),(62,'Indonesia'),(81,'Japan'),(234,'Nigeria'),(92,'Pakistan'),(7,'Russia'),(1,'United States')]
country_dial = {country:code for code,country in dial_codes} #exciting function!
print(country_dial)
country_dial = {country.upper():code for country,code in sorted(country_dial.items()) if code < 70}
print(country_dial)