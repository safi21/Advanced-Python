from datetime import datetime
import pytz

# function to find timezone of a given city. For example: it will take input 'dhaka' and return 'Asia/Dhaka'
def fixed_timezone(city):
    for tz in pytz.all_timezones:
        if city.capitalize() == tz[tz.find('/')+1:]:
            return tz
    else:
        print("Try again")
        exit()


# function to return time of an individual timezone.
def ret_time(time_zone):
    tz = pytz.timezone(time_zone)
    time = datetime.now(tz)
    return time

if __name__ == "__main__":
    city = input("Enter a city or Timezone: ")
    time_zone = fixed_timezone(city)
    time = ret_time(time_zone)
    fmt = '%Y-%m-%d %H:%M:%S'
    time = time.strftime(fmt)
    print(time)