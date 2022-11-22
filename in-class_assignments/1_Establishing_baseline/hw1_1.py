# I affirm that I have carried out my academic endeavors with full academic honesty.
# @MB (Manav Bilakhia)
# read the readme file for more information on how to run this script
import math
def star_travel_time(distance_light_years, percent_speed):
    speed_of_light = 299792458
    speed = speed_of_light * (percent_speed / 100)
    factor = 1 / math.sqrt(1 - (speed ** 2 / speed_of_light ** 2)) # lorentz factor
    convertion_light_year_in_meters = 9460730472580800 # 9.46073 * 10^15 meters conversion factor
    time_taken = distance_light_years * convertion_light_year_in_meters / (speed * factor)  # this is in light years
    time_in_years = time_taken / 31536000  # unit conversion
    return time_in_years

# print(star_travel_time(4.4, 100))
# print(star_travel_time(6.0, 100))
# print(star_travel_time(640.0, 100))
# print(star_travel_time(2500000.0, 100))

# print(star_travel_time(4.4, 50))
# print(star_travel_time(6.0, 50))
# print(star_travel_time(640.0, 50))
# print(star_travel_time(2500000.0, 50))

if __name__ == '__main__':
    distance_light_years = float(input("Enter the distance in light years: "))
    percent_speed = float(input("Enter the percent of the speed of light: "))
    print(star_travel_time(distance_light_years, percent_speed))
