def speed_conversion(unit1,unit2,unit3,unit4,value):
    dict1 = {
        "mm" : 1 ,
        "cm" : 2 ,
        "dm"  : 3 ,
        "m"  : 4 ,
        "dam": 5,
        "hm" : 6,
        "km" : 7
    }
    dict2 = {
        "s" : 1,
        "m" : 2,
        "h" : 3
    }
    sub1=dict1[unit1]-dict1[unit3]
    sub2=dict2[unit2]-dict2[unit4]
    if sub1 < 0 and sub2 < 0 :
        return ((value/10**abs(sub1))*60**abs(sub2))
    elif sub1 > 0 and sub2 < 0:
        return ((value * (10**sub1))*60**abs(sub2))
    elif sub1 < 0 and sub2 > 0 : 
        return ((value/10**abs(sub1))/60**sub2)
    elif sub1 > 0 and sub2 > 0 : 
        return ((value * (10**sub1))/60**sub2)