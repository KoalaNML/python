monthlist =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "," in date:
            month,day,year = date.replace(",","").split(" ")
            month = monthlist.index(month) + 1
        elif "/" in date:
            month,day,year = date.split("/")
            month = int(month)
        else:
            pass

        if 0 < int(day) <= 31 and 0 < month <= 12:
            print(f"{int(year)}-{month:02}-{int(day):02}")
            break
        else:
            raise ValueError
    
    except (ValueError,NameError):
        pass