def convertArea(x, unit1, unit2):
    areaD = {
    "sqmeter":1.0,
    "sqmillimeter":1000000.0,
    "sqcentimeter":10000.0,
    "sqkilometer":0.000001,
    "hectare":0.0001,
    "sqinch":1550.003,
    "sqfoot":10.76391,
    "sqyard":1.19599,
    "acre":0.0002471054,
    "sqmile":0.0000003861022
    }

    n=int(x)
    if (unit1 == "sqmeter") and (unit2 in areaD):
        factor1 = areaD[unit2]
        return factor1*x
    elif (unit1 in areaD) and (unit2 == "sqmeter"):
        factor1 = areaD[unit1]
        return x/factor1
    elif (unit1 in areaD) and (unit2 in areaD):
        factor1 = areaD[unit1]
        factor2 = areaD[unit2]
        return factor2*n/factor1
    else:
        return False