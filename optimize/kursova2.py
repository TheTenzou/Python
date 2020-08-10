from pulp import *

prob = LpProblem("Kursovaya", LpMaximize)

x = LpVariable.dicts("x", lowBound=0, upBound=1, cat="Integer")
