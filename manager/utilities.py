import datetime

def FormattedPhoneNumber(phoneNumber):
    if len(phoneNumber) > 7:
        phoneNumber = "(" + phoneNumber[0:3] + ") " + phoneNumber[3:6] + "-" + phoneNumber[6:10]
    else:
        phoneNumber = phoneNumber[0:3] + "-" + phoneNumber[3:7]

    return phoneNumber

def FormattedDate(dateToFormat):
    return dateToFormat.strftime("%b %d")