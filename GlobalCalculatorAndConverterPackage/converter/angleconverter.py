def deg_to_rad(angle_value:float)->float:
    PI = 3.1415926
    rad = "{:.6f}".format(float(angle_value) * (PI/180))
    return rad

def rad_to_deg(angle_value:float)->float:
    PI = 3.1415926
    return ("{:.6f}".format(float(angle_value) * (180/PI)))
    