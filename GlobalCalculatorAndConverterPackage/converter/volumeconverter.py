def convertVolume(unit1, unit2,x):
    areaD = {
    "cubicfoot":35.314666721489,
    "cubicinch":61023.744094732,
    "cubiccentimeter":1000000,
    "cubicmeter":1.0,
    "cubicyard":1.3079506193144,
    "liter":1000,
    "milliliter":1000000
    }

    n=int(x)
    if (unit1 == "cubicmeter") and (unit2 in areaD):
        factor1 = areaD[unit2]
        return factor1*x
    elif (unit1 in areaD) and (unit2 == "cubicmeter"):
        factor1 = areaD[unit1]
        return x/factor1
    elif (unit1 in areaD) and (unit2 in areaD):
        factor1 = areaD[unit1]
        factor2 = areaD[unit2]
        return factor2*n/factor1
    else:
        return False