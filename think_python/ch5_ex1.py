import time
current_time = time.time() # time since the epoch, with units of seconds. In Greenwich Mean Time.

# some conversions for working with current_time
sec_in_min = 60
sec_in_hour = sec_in_min * 60
sec_in_day = sec_in_hour * 24
sec_in_year = sec_in_day * 365

# converting current_time to years
years_elapsed = current_time // sec_in_year

# In the far future, the number of leap days will exceed a year, so we need to adjust the year count downward as necessary.
num_leap_days = years_elapsed // 4
if num_leap_days // 365 > 0: # if enough leap days have passed that they alone make up a year
	years_elapsed -= num_leap_days // 365

# converting current_time to days
days_elapsed = current_time // sec_in_day
print("It has been", days_elapsed, "days since the epoch, or", years_elapsed, "years and", days_elapsed % (years_elapsed * 365), "days.")

# to get a time of day, first find how many seconds have elapsed in the current day. Afterward, convert that to hour:minute:second format.
current_day_as_sec = current_time % sec_in_day

# numbers below are converted to int for readability
hour_now = int(current_day_as_sec // sec_in_hour)

if hour_now >= 7:
	hour_now_PDT = hour_now - 7 # PDT is -7
else:
	hour_now_PDT = hour_now - 7 + 24 # so we don't end up with a negative number

def get_ampm(hour):
	"""
	Accepts an hour in military time and returns its AM/PM reading.
	Output:
	ampm_time[0]: AM/PM hour as a string
	ampm_time[1]: either "AM" or "PM"
	"""

	ampm_time = ["", ""]
	hour_ampm = hour % 12
	ampm_time[0] = str(hour_ampm)

	if hour_ampm == hour:
		ampm_time[1] = "AM"
	else:
		ampm_time[1] = "PM"

	if ampm_time[0] == "0":
		ampm_time[0] = "12" # just a cosmetic change because we read 0 as 12 on the clock

	return ampm_time

hour_now_ampm = get_ampm(hour_now)
hour_now_PDT_ampm = get_ampm(hour_now_PDT)
min_now = int(current_day_as_sec % sec_in_hour // sec_in_min)
sec_now = int(current_day_as_sec % sec_in_min)

print("Time of day in GMT: " + str(hour_now) + ":" + str(min_now) + ":" + str(sec_now) + ", or " + hour_now_ampm[0] + ":" + str(min_now) + " " + hour_now_ampm[1]) 
print("In PDT: " + str(hour_now_PDT) + ":" + str(min_now) + ":" + str(sec_now) + ", or " + hour_now_PDT_ampm[0] + ":" + str(min_now) + " " + hour_now_PDT_ampm[1])
