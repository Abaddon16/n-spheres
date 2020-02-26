from math import gcd, pi, factorial, sqrt
from pprint import pprint as pp
import numpy as np
from operator import mul
from functools import reduce


class n_sphere:
    def __init__(self, dims, frac_top, frac_bot, pi_exp, rad_exp, equation_str):
        self.dims=dims
        self.top, self.bot=frac_top, frac_bot
        self.pi, self.rad=pi_exp, rad_exp
        self.eq_str=equation_str
    def __str__(self):
        return "******"+str(self.dims)+"******\n"+self.eq_str+"\n"

def simple_fact(x, y): #given x!/y! where (y>0)!=x, returns the bigger portion (whatever is left over), ie 3!/7!=1/840, returns 840
    res, x, y=1, max(x, y), min(x, y)
    while x>y: res, x=res*x, x-1
    return res
def factor(n):
    if n==1: return [1]
    i, factors, temp= 2, [], n
    while i*i < n:
        if n%i: i+=1+n%2
        else:
            n//=i
            factors.append(i)
    if n>1: factors.append(n)
    return factors
def reduce_mult(n, m):
    l1, l2=factor(n), factor(m)
    t=l1[:]
    return reduce(mul, list(np.setdiff1d(l1, l2, assume_unique=True))), reduce(mul, list(np.setdiff1d(l2, t, assume_unique=True)))
def gamma(n):
    return factorial(n/2) if n%2==0 else sqrt(pi)*(factorial(n+1)/(factorial((n+1)/2)*(2**(n+1))))


def sphere_eq(dims):
    if dims%2==0:
        k=dims//2
        ret={"frac_top": 1,"frac_bot": factorial(k),"pi_exp": k,"rad_exp": 2*k}
    else:
        k=(dims-1)//2
        top, bot=reduce_mult((2*(4**k)), simple_fact(2*k+1, k))
        ret={"frac_top": top,"frac_bot": bot,"pi_exp": k,"rad_exp": 2*k+1}
    return ret
def sphere_eq_str(params):
    f_t=str(params["frac_top"]) if params["frac_top"]>1 or params["frac_bot"]>1 else ""
    f_b=str(params["frac_bot"]) if params["frac_bot"]>1 else ""
    p_e=str(params["pi_exp"])
    r_e=str(params["rad_exp"])

    f_t=f_t+("\n" if f_b!="" else "")
    f_b="\n"+f_b if f_b!="" else ""
    bar='-'*len(f_b) if f_b!="" else ""
    p_e=("π" if float(p_e)>0 else "")+("^"+p_e if float(p_e)>1 else "")
    r_e=("r" if float(r_e)>0 else "")+("^"+r_e if float(r_e)>1 else "")

    string=' '*(len(bar)//2)+f_t+bar+p_e+r_e+f_b
    return string if string!="" else "0"

def create_sphere(dim, rad):
    eq=sphere_eq(dim)
    return n_sphere(dim, eq["frac_top"], eq["frac_bot"], eq["pi_exp"], eq["rad_exp"], sphere_eq_str(eq))
def sphere_list(limit, rad):
    return [create_sphere(i, rad) for i in range(0, limit+1)]


""" #testing
sph=sphere_list(25, 1)
for i in sph:
    print(i)
#"""
""" # maybe be able to calc internal vol, compare
for i, s in zip(range(len(sph)), sph):# show % of n-cube volume outside of n-sphere
    print(100*(2**i-s["unit vol"])/(2**i))
    #"""
