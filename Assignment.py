hrs = input("Enter Hours:")
h = float(hrs)

if h <= 40 :
    grosspay = hrs * 10.5
    print('grosspay')
else :
    extratime = hrs - 40
    grosspay = (hrs * 10.5) + (extratime * 15.75)
    print('grosspay')
