def get_seconds(time):
    seconds_pattern = {"d": 86400, "h": 3600, "m": 60, "s": 1}
    seconds = 0
    for time_part in time.split(" "):
        unit = time_part[-1:]
        value = time_part[:-1]
        seconds += seconds_pattern[unit] * int(value)
    return seconds


def format_time(seconds):
    hours = int(seconds / 3600)
    remainder = int(seconds - hours * 3600)
    minutes = int(remainder / 60)
    return (str(hours) + " hours" if hours > 0 else "") + (" and " if hours > 0 and minutes > 0 else " ") + \
           (str(minutes) + " minutes " if minutes > 0 else "")