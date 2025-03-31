def hotle_codst(nights) :
    return 140*nights

def plane_cost(city):
    if city == "pune":
        return 200
    if city == "mumbai":
        return 100
    if city == "delhi" :
        return 250
    if city == "banglore:":
        return 500
    
def car_rent(days):
    if days>= 7:
        40*days-50

    elif days>=3:
        return 40*days-20
    
    else :
        return 40*days
    
def trip_cost(city,days,money):
    return car_rent(days) + plane_cost(city) + hotle_codst(days) + money

a = input("enter n.o of days of trip")
b = input("enter a city pune,mumbaai,banglore,delhi")
c = input("extra money")

print("total expenditure is" , trip_cost(car_rent(a) + plane_cost(b) + hotle_codst(a) + c))