def decryption(message,type):
        return str(message.decode(type,'strict'))

def encryption(message,type):
        return str(message.encode(encoding=type))[2:-1]

