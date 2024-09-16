#Leap year
def leapyear(year):
    if year % 4 != 0:
        print ('not Leap year')
    elif year % 100 != 0:
        print ('Leap year')
    elif year % 400 == 0:
        print ('Leap year')        
    else:
        print ('No leap year')

leapyear(2024)
