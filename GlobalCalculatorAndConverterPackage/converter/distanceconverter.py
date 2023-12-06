def distance_conversion(unit1:str,unit2:str,value):
    dict = {
        "mm" : 1 ,
        "cm" : 2 ,
        "dm" : 3 ,
        "m" : 4 ,
        "dam" : 5,
        "hm" : 6,
        "km" : 7
    }
    sub=dict[unit1]-dict[unit2]
    if sub < 0 :
        return value/10**(abs(sub))
    else:
        return value * (10**sub)