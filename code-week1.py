def seconds_difference(time_1, time_2):
    return time_2 - time_1

def hours_difference(time_1, time_2):
    return (time_2 - time_1) / 3600

def to_float_hours(hours, minutes, seconds):
    if 0 <= minutes < 60  and  0 <= seconds < 60:
        return hours + (minutes / 60) + (seconds / 3600)

def get_hours(number):
    return number // 3600
def get_minutes(number):
    return (number % 3600) // 60
def get_seconds(number):
    return (number % 3600) % 60

# x = 4250
# print(get_hours(x))
# print(get_minutes(x))
# print(get_seconds(x))

def to_24_hour_clock(hours):
    return hours % 24
    
def time_to_utc(utc_offset, time):
    hours = time - utc_offset
    return to_24_hour_clock(hours)
    
def time_from_utc(utc_offset, time):
    hours = time + utc_offset
    return to_24_hour_clock(hours)


# print(time_to_utc(+0, 12.0))
# print(time_to_utc(+1, 12.0))
# print(time_to_utc(-1, 12.0))
# print(time_to_utc(-11, 18.0))
# print(time_to_utc(-1, 0.0))
# print(time_to_utc(-1, 23.0))

# print(time_from_utc(+0, 12.0))
# print(time_from_utc(+1, 12.0))
# print(time_from_utc(-1, 12.0))
# print(time_from_utc(+6, 6.0))
# print(time_from_utc(-7, 6.0))
# print(time_from_utc(-1, 0.0))
# print(time_from_utc(-1, 23.0))
# print(time_from_utc(+1, 23.0))
