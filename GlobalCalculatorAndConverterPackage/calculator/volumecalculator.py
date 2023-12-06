def sphereVol(rad):
    x = int(rad)
    return x*x*x*3.14*4/3

def cylinderVol(rad,ht):
    r = int(rad)
    h = int(ht)
    return 3.14*r*r*h

def cubeVol(side):
    s = int(side)
    return s*s*s

def CuboidVol(len,bre,ht):
    l = int(len)
    b = int(bre)
    h = int(ht)
    return l*b*h

def coneVol(rad,ht):
    r = int(rad)
    h = int(ht)
    return 3.14*r*r*h/3