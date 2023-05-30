def add_time(start, duration, day: str = "") :
    # Parse the start time and duration
    global end_day
    start_hour, start_minute = map(int, start[:-3].split(':'))
    start_period = start[-2:]
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Convert start hour to 24-hour format
    if start_period == 'PM' and start_hour != 12:
        start_hour += 12

    # Calculate the end time
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24

    # Convert end hour back to 12-hour format
    end_period = 'AM' if end_hour < 12 else 'PM'
    if end_hour > 12:
        end_hour -= 12
    # Determine the number of days later
    new_time = (start_hour + duration_hour + carry_hour) // 24

    # Determine the day of the week for the end time
    if day != '':
        start_day = day.lower().capitalize()
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + new_time) % 7
        end_day = days_of_week[end_day_index]

    # Construct the result string
    result = f"{end_hour}:{end_minute:02d} {end_period}" if end_hour != 0 else f"{12}:{end_minute:02d} {end_period}"
    if day != '':
        result += f", {end_day}"
    if new_time == 1:
        result += " (next day)"
    elif new_time > 1:
        result += f" ({new_time} days later)"

    return result