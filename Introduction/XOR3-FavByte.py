from Crypto.Util.number import *
import traceback


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
            return_bytes += byte
    return return_bytes


def hex_to_string(hex) -> str:
    return ''.join([chr(int(''.join(c), 16)) for c in zip(hex[0::2],hex[1::2])]).replace(';', '\n- ')


ENCRYPTED_HEX: str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

encrypted_bytes = bytes.fromhex(ENCRYPTED_HEX)

for i in range(256):
    
    # for byte_index in range(len(encrypted_bytes)):
    #     try:
    #         byte = encrypted_bytes[byte_index]
    #         encrypted_bytes_front = encrypted_bytes[:byte_index-1] if byte_index != 0 else b''
    #         encrypted_bytes_back = encrypted_bytes[byte_index+1:]

    #         byte = bytes.fromhex(xor(byte, i))
    #         decrypted_bytes = encrypted_bytes_front + byte + encrypted_bytes_back
    #         #decrypted_hex = decrypted_bytes.decode('utf-8')
    #         flag = decrypted_bytes.decode('utf-8')
    #         print(f"byte={byte} bIndex={byte_index:02} flag={flag}")
    #     except Exception as e:
    #         traceback.print_exc()

    try:
        flag = xor_each(encrypted_bytes, i).decode('utf-8')
        print(f"Byte={i}", flag, "\n\n")

        # Byte=16 crypto{0x10_15_my_f4v0ur173_by7e}
    except Exception as e:
        pass
    
