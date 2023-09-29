def get_hours(number):
    return number // 3600
def get_minutes(number):
    return (number % 3600) // 60
def get_seconds(number):
    return (number % 3600) % 60

x = 4250
print(get_hours(x))
print(get_minutes(x))
print(get_seconds(x))

def to_24_hour_clock(hours):
    return hours % 24
    
def time_to_utc(utc_offset, time):
    hours = time - utc_offset
    return to_24_hour_clock(hours)
    
def time_from_utc(utc_offset, time):
    hours = time + utc_offset
    return to_24_hour_clock(hours)


print(time_to_utc(+0, 12.0))
print(time_to_utc(+1, 12.0))
print(time_to_utc(-1, 12.0))
print(time_to_utc(-11, 18.0))
print(time_to_utc(-1, 0.0))
print(time_to_utc(-1, 23.0))

print(time_from_utc(+0, 12.0))
print(time_from_utc(+1, 12.0))
print(time_from_utc(-1, 12.0))
print(time_from_utc(+6, 6.0))
print(time_from_utc(-7, 6.0))
print(time_from_utc(-1, 0.0))
print(time_from_utc(-1, 23.0))
print(time_from_utc(+1, 23.0))
