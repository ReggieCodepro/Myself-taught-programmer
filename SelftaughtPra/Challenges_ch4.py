#chaper 4 challenges

#challenge 1
def f(x=2):
    """
    Returns the sqaure root of x
    :param x: int. which equals 2
    
    """
    return x**x
print(f())

#challenge 2
def Q(f="hello, world"):
    """
    Returns a string
    :param f: string which equals hello, world.
    """
    return f

print(Q())

#challenge 3

def substrac_it(x, y, r, z=35, w=15):
    """
    repuired param x: int.  
    repuired param y: int.
    repuired param r: int.
    optional param z: int that equals 35
    optional param w: int that equals 15
    returns: x minus y minus r minus z minus w
    """
    return x - y - r - z - w

result = substrac_it(20, 22, 12)
print(result)

#challenge 4
def divid_by(x=18):
    """
    optional param: int. x is equal to 18
    returns x divided by 2
    """
    return x // 2
print(divid_by())

def multi_by(x=18):
    """
    optional param: int. x is equal to 18
    returns x mulitply by 2
    """
    return x * 2
print(multi_by())

#challenge 5
def convert(string):
    try:
        return float(string)
    except ValueError:
        print("could not convert the string into a float")
c = convert("55.0")
print(c)


