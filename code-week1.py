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