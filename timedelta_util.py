import datetime as dt

def actual_hours(delta_time):
    '''
    Gets the number of hours represented by the seconds
    property to hours. Does not include smaller units.
    '''
    return delta_time.seconds // 3600


def actual_minutes(delta_time):
    '''
    Gets the number of minutes represented by the seconds
    property to hours. Does not include smaller or
    larger units.
    '''
    return delta_time.seconds % 3600 // 60


def actual_seconds(delta_time):
    '''
    Gets the number of seconds represented by the seconds
    property to hours. Does not include larger units.
    '''
    return delta_time.seconds % 3600 % 60


# Test code
if __name__ == "__main__":
    d = dt.timedelta(days=1, hours=2, minutes=15, seconds=30)
    print(actual_hours(d))
    print(actual_minutes(d))
    print(actual_seconds(d))
