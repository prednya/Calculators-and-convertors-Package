def phy_speed1(dist,t):
    return dist/t

def phy_speed2(u,a,t):
    return u+(a*t)

def phy_speed3(v,a,dist):
    return (v**2-(2*a*dist))**0.5