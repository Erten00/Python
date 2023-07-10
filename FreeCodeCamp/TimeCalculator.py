def add_time(start_time, duration, start_day=None):
    # Parse the start time
    start_components = start_time.split(':')
    start_hour = int(start_components[0])
    start_minute = int(start_components[1][:-3])  # Remove the space and AM/PM from minutes
    period = start_components[1][-2:]  # Extract AM/PM

    # Parse the duration
    duration_components = duration.split(':')
    duration_hour = int(duration_components[0])
    duration_minute = int(duration_components[1])

    # Convert start hour to 24-hour format
    if period == 'PM':
        start_hour += 12

    # Calculate the end time
    end_minute = (start_minute + duration_minute) % 60
    carry_hour = (start_minute + duration_minute) // 60
    end_hour = (start_hour + duration_hour + carry_hour) % 24

    # Determine if it's AM or PM for the end time
    if end_hour < 12:
     end_period = 'AM'
    elif end_hour == 12 and end_minute == 0:
      end_period = 'PM'
      end_hour = 12
    else:
     end_period = 'PM'
     end_hour -= 12

    # Convert 0 to 12 for end hour
    if end_hour == 0:
     end_hour = 12


    # Calculate the number of days later
    days_later = (start_hour + duration_hour + carry_hour) // 24

    # Calculate the day of the week if provided
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if start_day:
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]

    # Prepare the output string
    output = f"{end_hour}:{end_minute:02d} {end_period}"

    if start_day:
        output += f", {end_day}"

    if days_later == 1:
        output += " (next day)"
    elif days_later > 1:
        output += f" ({days_later} days later)"

    return output