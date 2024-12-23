def is_leap(year):
    leap = False
    if year%100==0:
        if year%400==0:
            leap=True
    elif year%4==0:
        leap=True
    
    return leap

year = int(input("Enter year:"))
if is_leap(year) is True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")