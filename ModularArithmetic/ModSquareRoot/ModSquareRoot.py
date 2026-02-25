from pathlib import Path

script_dir = Path(__file__).resolve().parent
target_file = script_dir / 'output_abe0beb359a950c8a0a9300897528a9d.txt'
variables_dict = {}

with open(target_file, 'r') as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line or line.startswith('#'):  # Skip blank lines or comments
            continue
        try:
            name, value = line.split('=', 1)
            # Store in the dictionary, stripping whitespace from key and value
            variables_dict[name.strip()] = value.strip()
        except ValueError:
            print(f"Invalid format found in line: {line}")

# # Access variables using the dictionary:
# print(f"a is: {variables_dict['a']}")
# print(f"p is: {variables_dict['p']}")

# # You might need to convert values to the appropriate type (e.g., int, float)
print(type(variables_dict['p']))

if 'p' in variables_dict:
    var_b_int = int(variables_dict['p'])
    variables_dict['p'] = int(variables_dict['p'])
    print(f"p as int is: {variables_dict['p']}")

print(type(variables_dict['p']))

# ---------------------------------------------------------------------------------------------------

def Legendre(a,p):
    """Legendre's symbol: (a|p) === a^( (p-1)/2 ) mod p"""

    return pow(a, ( (p-1)//2 ), p)

