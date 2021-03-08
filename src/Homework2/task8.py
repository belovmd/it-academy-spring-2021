"""Write a function, which takes a non-negative integer (seconds) as input and returns

the time in a human-readable format (HH:MM:SS)
HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures."""

# 5 que task in www.codewars.com


def make_readable(seconds):
    if seconds > 3599:
        hours_ = int(seconds // 3600)
        minutes_ = int(((seconds / 3600 - hours_) * 60) // 1)
        seconds_ = int(seconds - hours_ * 3600 - minutes_ * 60)
        if seconds_ == 60:
            minutes_ += 1
            seconds_ = ''
    elif seconds > 59:
        hours_ = ''
        minutes_ = int(seconds // 60)
        seconds_ = int((seconds / 60 - minutes_) * 60)
    else:
        hours_ = ''
        minutes_ = ''
        seconds_ = seconds
    if len(str(hours_)) == 2:
        hours = str(hours_)
    elif len(str(hours_)) == 1:
        hours = '0' + str(hours_)
    else:
        hours = '00'
    if len(str(minutes_)) == 2:
        minutes = str(minutes_)
    elif len(str(minutes_)) == 1:
        minutes = '0' + str(minutes_)
    else:
        minutes = '00'
    if len(str(seconds_)) == 2:
        sec = str(seconds_)
    elif len(str(seconds_)) == 1:
        sec = '0' + str(seconds_)
    else:
        sec = '00'
    return "{0}:{1}:{2}".format(hours, minutes, sec)


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
