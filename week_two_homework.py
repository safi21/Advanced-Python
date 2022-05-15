from datetime import datetime
import pytz

#converts city to timezone eg: dhaka to 'Asia/Dhaka'
def tz_converter(city): 
    for tz in pytz.all_timezones:
        if city.capitalize() in tz:
            break
    return tz

#function to find individual timezone eg: 'Asia/Dhaka'
def ind_tz(time_zone):
    tz_city = pytz.timezone(tz_converter(city))
    time = datetime.now(tz_city)
    return time

if __name__ == "__main__":
    city = input("Enter a timezone: ")
    time = ind_tz(city)
    print(time)

