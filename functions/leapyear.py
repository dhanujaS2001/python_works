def leapyear(year):
    if year%100==0 and year%400==0:
        return  True
    elif year%100!=0 and year%4==0:
        return True
    else:
        return False
print(leapyear(1900))