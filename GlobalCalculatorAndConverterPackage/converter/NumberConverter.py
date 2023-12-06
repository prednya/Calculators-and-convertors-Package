def binary_to_octal(string_num):
    num=int(string_num,2)
    oct_num=oct(num)
    return oct_num[2:]

def binary_to_decimal(number):
    return str(int(number,2))

def binary_to_hex(string_num):
    num=int(string_num,2)
    hex_num=hex(num)
    return hex_num[2:]

def octal_to_binary(string_num):
    res=bin(int(string_num,8))
    return res[2:]

def octal_to_hex(string_num):
    num=int(string_num,8)
    hex_num=hex(num)
    ans=hex_num[2:]
    return ans.upper()
    
def octal_to_decimal(string_num):
    res=int(string_num,8)
    return str(res)

def decimal_to_binary(number:str):
    return bin(int(number))[2:]

def decimal_to_hex(dec):
    return hex(int(dec))[2:]

def decimal_to_octal(dec):
    return oct(int(dec))[2:]

def hex_to_binary(value):
    return bin(int(value, 16))[2:]

def hex_to_decimal(hexValue:str):
    ans=0
    count=0
    for i in hexValue[::-1]:
        if i=='0':
            ans=ans+(16**count)*0
        elif i=='1':
            ans=ans+(16**count)*1
        elif i=='2':
            ans=ans+(16**count)*2
        elif i=='3':
            ans=ans+(16**count)*3
        elif i=='4':
            ans=ans+(16**count)*4
        elif i=='5':
            ans=ans+(16**count)*5
        elif i=='6':
            ans=ans+(16**count)*6
        elif i=='7':
            ans=ans+(16**count)*7
        elif i=='8':
            ans=ans+(16**count)*8
        elif i=='9':
            ans=ans+(16**count)*9
        elif i=='a':
            ans=ans+(16**count)*10
        elif i=='b':
            ans=ans+(16**count)*11
        elif i=='c':
            ans=ans+(16**count)*12
        elif i=='d':
            ans=ans+(16**count)*13
        elif i=='e':
            ans=ans+(16**count)*14
        elif i=='f':
            ans=ans+(16**count)*15
        count= count+1

    return str(ans)

def hex_to_octal(hexValue):
    return oct(int(hexValue,16))[2:]

