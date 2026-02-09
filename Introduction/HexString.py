flag_hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

flag_bytes = bytes.fromhex(flag_hex)

print(flag_bytes)

flag_hex2 = flag_bytes.hex()

print(flag_hex2)