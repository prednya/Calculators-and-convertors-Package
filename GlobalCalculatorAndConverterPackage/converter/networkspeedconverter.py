def network_conversion(unit1,unit2,value):
    dict1 = {
        "bps" : 1 ,
        "Kbps" : 4 ,
        "Mbps"  : 7 ,
        "Gbps"  : 10 
    }
    dict2 = {
        "Bps" : 1,
        "KBps" : 4,
        "MBps" : 7,
        "GBps" : 10
    }
    sub=0
    if unit1 in dict1 and unit2 in dict2 :
        value=value/8
        sub=dict1[unit1]-dict2[unit2]
    elif unit1 in dict2 and unit2 in dict1 :
        value=value*8
        sub=dict2[unit1]-dict1[unit2]
    elif unit1 in dict1:
        sub=dict1[unit1]-dict1[unit2]
    else:
        sub=dict2[unit1]-dict2[unit2]
    
    if sub < 0:
        return (value/10**abs(sub))
    elif sub > 0:
        return (value * (10**sub))
