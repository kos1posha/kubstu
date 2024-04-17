def jog(speed_start, speed_end):
    day_count = 0
    while speed_start < speed_end:
        speed_start *= 1.10
        day_count += 1
    return day_count