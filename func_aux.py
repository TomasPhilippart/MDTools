class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(a, b):
    """Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
    """
    # r = gcd(a,b) i = multiplicitive inverse of a mod b
    #      or      j = multiplicitive inverse of b mod a
    # Neg return values for i or j are made positive mod b or a respectively
    # Iterateive Version is faster and uses much less stack space
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a  # Remember original a/b to remove
    ob = b  # negative values from return results
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  # If neg wrap modulo orignal b
    if ly < 0:
        ly += oa  # If neg wrap modulo orignal a
    # return a , lx, ly  # Return only positive values
    return lx

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def soma_pot_2_aux(x):
    v = []
    # Converting the decimal number 
    # into its binary equivalent. 
    while (x > 0): 
        v.append(int(x % 2)) 
        x = int(x / 2) 
    
    powers = []
    # Displaying the output when 
    # the bit is '1' in binary 
    # equivalent of number. 
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            powers = [i] + powers

    return powers

def soma_pot_2(x): 
    powers = soma_pot_2_aux(x)

    display = f"{x} = "
    display2 = "= "

    for i in powers:
        display += f"2^{i} + "
    
    for i in powers:
        display2 += f"{2**i} + "

    return display[:-2] + display2[:-3]

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print(f"{bcolors.WARNING}Tem de ser um inteiro!{bcolors.ENDC}")
       continue
    else:
       return userInput 

def saunderson(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

def diofantina(a,b,c):
    q,r = divmod(a,b)
    if r == 0:
        return ( [0, c//b] )
    else:
        sol = diofantina(b,r,c)
        u = sol[0]
        v = sol[1]
        return ( [v, u - q*v] )
