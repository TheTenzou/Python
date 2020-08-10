import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    dif = [1, 1, 1, 2, 2, 3, 3, 3, 2, 1, 2, 1, 2, 2, 2, 2, 1, 2]
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    res = [1, 1, 1, 2, 1, 2, 4, 3, 2, 1, 2, 1, 3, 2, 3, 3, 2, 5]
    eff = [2, 2, 2, 1, 3, 4, 5, 6, 1, 2, 3, 4, 2, 1, 2, 3, 1, 5]
    ress = 0
    for i in range(5):
        for j in range(18):
            ress = ress + x[j*5+i] * eff[j]
    return ress*-1


def constraintRes(x):
    res = [1, 1, 1, 2, 1, 2, 4, 3, 2, 1, 2, 1, 3, 2, 3, 3, 2, 5]
    ress = 50
    for i in range(5):
        for j in range(18):
            ress = ress - x[j*5+i] * res[j]
    return ress


def constraintLoad(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    res = 0
    for i in range(5):
        tmp = 0
        for j in range(18):
            tmp = tmp + x[j*5+i] * len[j]
        if tmp > 8:
            res = 1
    return res


def consr1(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    tmp = 8
    for i in range(18):
        tmp = tmp - x[i*5+0]*len[i]
    return tmp


def consr2(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    tmp = 8
    for i in range(18):
        tmp = tmp - x[i*5+1]*len[i]
    return tmp


def consr3(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    tmp = 8
    for i in range(18):
        tmp = tmp - x[i*5+2]*len[i]
    return tmp


def consr4(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    tmp = 8
    for i in range(18):
        tmp = tmp - x[i*5+3]*len[i]
    return tmp


def consr5(x):
    len = [1, 1, 1, 2, 3, 4, 5, 2, 2, 1, 3, 1, 2, 2, 3, 3, 2, 4]
    tmp = 8
    for i in range(18):
        tmp = tmp - x[i*5+4]*len[i]
    return tmp


x0 = [0 for y in range(18*5)]
b = (0, 1)
bnds = tuple([b for y in range(18*5)])
con1 = {'type': 'eq', 'fun': constraintRes}
#con2 = {'type': 'eq', 'fun': constraintLoad}
con3 = {'type': 'ineq', 'fun': consr1}
con4 = {'type': 'ineq', 'fun': consr2}
con5 = {'type': 'ineq', 'fun': consr3}
con6 = {'type': 'ineq', 'fun': consr4}
con7 = {'type': 'ineq', 'fun': consr5}
cons = [con1, con3, con4, con5, con6, con7]
#sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
#sol = minimize(objective, x0, method='SLSQP', bounds=bnds)
sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
#print(sol.x)
tmp = sol.x

#for i in range(18*5):
#    tmp[i] = math.floor(tmp[i])

print(tmp)
print(sol.fun)
print(objective(tmp))
print(sol.success)
print('constr res = ', constraintRes(tmp))
print('constr1 = ', consr1(tmp))
print('constr2 = ', consr2(tmp))
print('constr3 = ', consr3(tmp))
print('constr4 = ', consr4(tmp))
print('constr5 = ', consr5(tmp))
