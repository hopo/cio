def time_converter(time):
    hour = int(time[:2])
    apm = 'a.m.'
    if hour > 11:
        apm = 'p.m.'
        hour -= 12
    if hour == 0:
        hour = 12

    return '{}{} {}'.format(hour, time[2:], apm)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
