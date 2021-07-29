import numpy as np
from pysr import pysr, best
from pysr.sr import best_callable, best_tex

from matplotlib import pyplot as plt

from pendelum import X, tstep


# Learn equations for each mass separately: (x,y) ~ t 
eqns1 = pysr(
    X[:,0:1],
    tstep,
    niterations=5,
    binary_operators=["+", "*"],
    unary_operators=[
        "cos",
        "sin",  
        "square",
    ]
)

eqns2 = pysr(
    X[:,2:3],
    tstep,
    niterations=5,
    binary_operators=["+", "*", '-'],
    unary_operators=[
        "cos",
        "sin",  
        "square",
    ]
)

mdl1 = best_callable(eqns1)
mdl2 = best_callable(eqns2)

# PySRFunction(X=>7.51104841189264*(0.364879714483083*x0*(4.308792032169*x0**2 - 1.0965774) + 1)**2)
# PySRFunction(X=>7.53803272208484*(-0.364226038971166*x0**2*sin(x0)*cos(9.11820942355129*(x0 + 0.0402025667122339)**2) + 1)**2)