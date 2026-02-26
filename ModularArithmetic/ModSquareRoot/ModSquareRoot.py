from pathlib import Path
import argparse

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
#print(type(variables_dict['p']))

if 'p' in variables_dict:
    p = int(variables_dict['p'])
    variables_dict['p'] = int(variables_dict['p'])
    # print(f"p as int is: {p}")

if 'a' in variables_dict:
    a = int(variables_dict['a'])
    variables_dict['a'] = int(variables_dict['a'])
    # print(f"a as int is: {a}")

# ---------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser(description="-v | --verbose for intermediary variables")
parser.add_argument("-v", "--verbose", action='store_true', help="enable verbose output")
args = parser.parse_args()

# usage: args.verbose (bool)

# ---------------------------------------------------------------------------------------------------


def isEquivalent(a: int, b: int, p: int):
    """compares if a, b are equivalent mod p"""
    return (a % p) == (b % p)

def Legendre(a,p):
    """Legendre's symbol: (a|p) === a^( (p-1)/2 ) mod p"""

    return pow(a, ( (p-1)//2 ), p)

format_indent = "-> "

# All ≡ are taken to mean (mod p) unless stated otherwise.

# Input: p an odd prime, and an integer n .
# Step 0: Check that n is indeed a square: (n | p) must be ≡ 1 .
# Step 1: By factoring out powers of 2 from p - 1, find q and s such that p - 1 = q * (2 ^ s) with q odd .
    # If p ≡ 3 (mod 4) (i.e. s = 1), output the two solutions r ≡ ± n ^ ((p+1)/4) .
# Step 2: Select a non-square z such that (z | p) ≡ -1 and set c ≡ z ^ q .
# Step 3: Set r ≡ n ^ ((q+1)/2), t ≡ n^q, m = s .
# Step 4: Loop the following:
    # If t ≡ 1, output r and p - r .
    # Otherwise find, by repeated squaring, the lowest i, 0 < i < m , such that t^2^i ≡ 1 .
    # Let b ≡ c^2^(m - i - 1), and set r ≡ rb, t ≡ t*b^2, c ≡ b^2 and m = i .
print("Step 0" + '.' * 50)
if (Legendre(a, p) != 1):
    print("No solutions")
print("Step 1" + '.' * 50)
q: int = 1 # q must be odd
s = 0
while((p-1)% pow(2,s)==0):
        s+=1
s-=1
q=int((p-1)// pow(2,s))# p-1=q*2^s
if s == 1:
    print(f"SOLUTIONS FOUND: r ≡ ±{pow(a, (p+1)//4), p}")

if args.verbose:
    print(format_indent, f"q={q}, s={s}")
print("Step 2" + '.' * 50)
z = 1
while Legendre(z, p) != p-1: z += 1
c = pow(z, q, p)

if args.verbose:
    print(format_indent, f"c={c}")
print("Step 3" + '.' * 50)
r = pow(a, (q+1)//2, p)
t = pow(a, q, p)
m = s

if args.verbose:
    print(format_indent, f"r={r}, t={t}, m={m}")

print("Step 4" + '.' * 50)
while t % p != 1:
    i=0
    div=False
    while(div==False):
        i+=1
        t=int(pow(t,2))%p
        if(t%p==1):
            div=True
    b = pow(c, 2^(m-i-1), p)
    r = (r*b) % p
    t = (t * b ^ 2) % p
    c = pow(b, 2, p)
    m = i
    if args.verbose:
        print(f"b={b}", f"r={r}", f"t={t}", f"c={c}", f"m={m}", sep='\n')
    

    
print("FINAL RESULTS")
print (format_indent, f"r={r}")
print(format_indent, f"p-r={p-r}")