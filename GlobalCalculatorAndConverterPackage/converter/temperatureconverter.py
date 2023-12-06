def fahrenheit(temp):
    temp_int = int(temp)
    c_temp = int((temp_int - 32)* 5 / 9)
    k_temp = c_temp + 273.15
    return (c_temp,k_temp)

def celsius(temp):
    temp_int = int(temp)
    f_temp = int((temp_int *(9 / 5)) + 32) 
    k_temp = temp_int + 273.15
    return (f_temp,k_temp)

def kelvin(temp):
    temp_int = int(temp)
    c_temp = temp_int - 273.15
    f_temp = int((c_temp * (9 / 5)) + 32)
    return (c_temp,f_temp)