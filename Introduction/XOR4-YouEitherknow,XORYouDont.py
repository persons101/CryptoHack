ENCRYPTED_KEY = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

from Crypto.Util.number import *
import base64

def xor(*args, **kwords: str) -> str:
    """
    Docstring for xor
    
    :param args: Strings to be xor'ed. May be regular or hex-string (reg untested)
    :type args: str
    :param kwords: If the first arg is a hex-string, arg1=True. Second arg-> arg2=True, etc. 
    :type kwords: str
    :return: Returns a hex string with the result of the xor
    :rtype: str
    """
    char_long: int
    result: int = 0
    arg_num = 1
    result_str = ""

    for arg in args:
        arg_num_str = "arg" + str(arg_num) #
        
        if (type(arg) == int) and not kwords.get(arg_num_str):
            result = result ^ arg
        elif type(arg) == bytes:
            result = result ^ bytes_to_long(arg)
        elif kwords.get(arg_num_str):
            arg = bytes.fromhex(str(arg))
            result = result ^ bytes_to_long(arg)
        else:
            for char in arg:
                char_long = ord(char)
                result = result ^ char_long
        
        result_hex = hex(result)
        result_hex = result_hex[2:]
        arg_num += 1
    return result_hex

def xor_each(arg1, arg2: int):
    if type(arg1) == int:
        arg1 = long_to_bytes(arg1)
    elif type(arg1) == str:
        try:
            arg1 = bytes.fromhex(arg1)
        except Exception:
            arg1 = arg1.encode()
    arg1: bytes

    # if type(arg2) == int:
    #     arg2 = long_to_bytes(arg2)
    # elif type(arg2) == str:
    #     try:
    #         arg2 = bytes.fromhex(arg2)
    #     except Exception:
    #         arg2 = arg2.encode()
    # arg2: bytes

    return_bytes = b''
    for byteIndex in range(len(arg1)):
            byte = arg1[byteIndex]
            encrypted_bytes_front = arg1[:byteIndex-1] if byteIndex != 0 else b''
            encrypted_bytes_back = arg1[byteIndex+1:]

            byte = bytes.fromhex(xor(byte, arg2))
            return_bytes += long_to_bytes(byte[-1])
    return return_bytes

def xor_each_byte(arg1, arg2):
    if type(arg1) == int:
        arg1 = long_to_bytes(arg1)
    elif type(arg1) == str:
        try:
            arg1 = bytes.fromhex(arg1)
        except Exception:
            arg1 = arg1.encode()
    arg1: bytes

    # if type(arg2) == int:
    #     arg2 = long_to_bytes(arg2)
    # elif type(arg2) == str:
    #     try:
    #         arg2 = bytes.fromhex(arg2)
    #     except Exception:
    #         arg2 = arg2.encode()
    # arg2: bytes

    return_bytes = b''
    for byteIndex in range(len(arg1)):
            byteA = arg1[byteIndex]
            byteB = arg2[byteIndex % len(arg2)]

            byte = long_to_bytes(byteA ^ byteB)
            return_bytes += byte
    return return_bytes


def hex_to_string(hex) -> str:
    return ''.join([chr(int(''.join(c), 16)) for c in zip(hex[0::2],hex[1::2])]).replace(';', '\n- ')


encrypted_bytes = bytes.fromhex(ENCRYPTED_KEY)

TOTAL_FLAG_LENGTH = len(encrypted_bytes)

key_format_front = "crypto{"
key_format_front = key_format_front.encode()
key_format_front_size = len(key_format_front)

key_format_back = "}"
key_format_back = key_format_back.encode()
key_format_back_size = len(key_format_back)

key_format = key_format_front + b'0' * (TOTAL_FLAG_LENGTH - (key_format_front_size + key_format_back_size)) + key_format_back

#print(f"{encrypted_bytes.decode()}\n")


decrypted_flagA = xor( encrypted_bytes, key_format)
flagA = hex_to_string(decrypted_flagA)
print(f"A: {flagA}\n")

# decrypted_flagB = xor_each(encrypted_bytes, bytes_to_long(key_format))
# flagB = decrypted_flagB.decode()
# print(f"{flagB}\n")

# decrypted_flagC = xor_each_byte(encrypted_bytes, key_format)
# flagC = decrypted_flagC.decode()
# print(flagC)

key_format_line2 = "myXORkey".encode()
key_format_line2_size = len(key_format_line2)
key_format2 = key_format_front + key_format_line2 + b'0'* (TOTAL_FLAG_LENGTH - (key_format_front_size + key_format_back_size + key_format_line2_size)) + key_format_back

decrypted_flagD = xor( encrypted_bytes, key_format2)
flagD = hex_to_string(decrypted_flagD)
print(f"D: {flagD}\n")

# FLAG E == FLAG D
# decrypted_flagE = xor_each_byte( encrypted_bytes, key_format2)
# flagE = decrypted_flagE.decode()
# print(f"{flagE}\n")

key_format_line3 = "myXORke%r~n-LQV'm>7:".encode()
key_format_line3_size = len(key_format_line3)

key_format3 = key_format_front + key_format_line3 + b'0' * (TOTAL_FLAG_LENGTH - (key_format_front_size + key_format_line3_size + key_format_back_size)) + key_format_back
decrypted_flagF = xor(encrypted_bytes, key_format3)
flagF = hex_to_string(decrypted_flagF)
print("F:", flagF, "\n")

key_guess_G = b'myXORkey'
hex_flagG = xor(ENCRYPTED_KEY, key_guess_G)
flagG = hex_to_string(hex_flagG)
print("G:", flagG)

key_guess_H = b'myXORkex'
byte_flagH = xor_each(ENCRYPTED_KEY, key_guess_H)
flagH = byte_flagH.decode()
print("H:", f"{key_guess_H}:", flagH)

byte_flagI = xor_each(ENCRYPTED_KEY, key_guess_G)
flagI = byte_flagI.decode()
print(f"I: {flagI}")

# flagH : flagI :: v : w
## ^^ Worthless


###Solution
#J: b'myXORkey': crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
# This one gave me struggles due an initally poor implementation of xor_each_byte

key_guess_J = b'myXORkey'
byte_flagJ = xor_each_byte(ENCRYPTED_KEY, key_guess_J)
flagJ = byte_flagJ.decode()
print(f"J: {key_guess_J}: {flagJ}")