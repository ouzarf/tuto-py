# function eval

r = eval("(-1, 1)")

C = raw_input("C=? ")
C = float(C)
F = (9./5)*C + 32
print( F )

r = eval(' 5.1 ')
r

i1 = eval(input("Give input: "))
i2 = eval(input("Give input: "))
r = i1 + i2
print ("%s + %s becomes %s\nwith value %s" % \
(type(i1), type(i2), type(r), r))

i1 = eval(input("Give input: "))
i2 = eval(input("Give input: "))
r = i1 + i2
print ("%s + %s becomes %s\nwith value %s" % \
(type(i1), type(i2), type(r), r))

from math import * # make all math functions available

formula =input("Give a formula involving x: ")
x = eval(input("Give x: "))

result = eval(formula)
print( "%s for x=%g yields %g" % (formula, x, result))

def f(x):
    return sin(x)*cos(3*x) + x**2



 x=0
formula = input("Write a formula involving x: ")
code = """
def f(x):
    return %s
    """ % formula
exec(code)


x = 0
while x is not None:
    x = eval(input("Give x (None to quit): "))
    if x is not None:
        print( "f(%g)=%g" % (x, f(x)))


