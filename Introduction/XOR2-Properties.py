from Crypto.Util.number import *

### Properties of XOR operator
# Commutative: A ⊕ B = B ⊕ A
# Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
# Identity: A ⊕ 0 = A
# Self-Inverse: A ⊕ A = 0


### Specific challenge
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

def xor(*args: str, **kwords: str) -> str:
    """
    Docstring for xor
    
    :param args: Strings to be xor'ed. May be regular or hex-string
    :type args: str
    :param kwords: If the first arg is not a hex-string, arg1=True. Second arg-> arg2=True, etc. 
    :type kwords: str
    :return: Returns a string with the result of the xor
    :rtype: str
    """
    char_long: int
    result: int = 0
    arg_num = 1
    result_str = ""

    for arg in args:
        arg_num_str = "arg" + str(arg_num) #
        if not kwords.get(arg_num_str):
            arg = bytes.fromhex(arg)
            result = result ^ bytes_to_long(arg)
        else:
            for char in arg:
                char_long = ord(char)
                result = result ^ char_long
        
        result_hex = hex(result)
        result_hex = result_hex[2:]
        arg_num += 1
    return result_hex
def hex_to_string(hex) -> str:
    return ''.join([chr(int(''.join(c), 16)) for c in zip(hex[0::2],hex[1::2])]).replace(';', '\n- ')


KEY2 = xor(KEY1, "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY3 = xor(KEY2, "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG = xor(KEY1, KEY2, KEY3, "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

FLAG_STR = hex_to_string(FLAG)

print(f"{FLAG_STR}")