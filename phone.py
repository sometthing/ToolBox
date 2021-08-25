from opencage.geocoder import OpenCageGeocode
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

print("""

*----===------====----*
| phone number lookup |
*=====-----====-------*

█▀▀█ █░░█ █▀▀█ █▀▀▄ █▀▀ 
█░░█ █▀▀█ █░░█ █░░█ █▀▀ 
█▀▀▀ ▀░░▀ ▀▀▀▀ ▀░░▀ ▀▀▀

&=======----====--====----&
| Created by TheGhostRoot |
&---========-------======-&

""")

numberF = input("[+} Enter the phone number country code with + : ")
numberS = input("[+} Enter the phone number " + numberF + " ")
number = numberF+numberS
print(number)
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
