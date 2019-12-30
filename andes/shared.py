"""
Shared constants and delayed imports.

Known issues ::

    1) The delayed import of pandas and newton_krylov will cause a ``RuntimeWarning``

    RuntimeWarning: numpy.ufunc size changed, may indicate binary incompatibility. Expected 192 from C header,
    got 216 from PyObject
        return f(*args, **kwds)
"""
# from andes.utils.lazyimport import LazyImport
#
# # ----------------------------------------
# # Packages
# np = LazyImport('import numpy')
# pd = LazyImport('import pandas')
# tqdm = LazyImport('from tqdm import tqdm')
# plt = LazyImport('from matplotlib import pyplot')
# mpl = LazyImport('import matplotlib')
# umfpack = LazyImport('from cvxopt import umfpack')
# cvxopt = LazyImport('import cvxopt')
# coloredlogs = LazyImport('import coloredlogs')
# Process = LazyImport('from multiprocessing import Process')
# # ----------------------------------------
#
# # ----------------------------------------
# # Types
# ndarray = LazyImport('from numpy import ndarray')
# spmatrix = LazyImport('from cvxopt import spmatrix')
# matrix = LazyImport('from cvxopt import matrix')
# sparse = LazyImport('from cvxopt import sparse')
# spdiag = LazyImport('from cvxopt import spdiag')
# # ----------------------------------------
#
# # ----------------------------------------
# # function calls
# newton_krylov = LazyImport('from scipy.optimize import newton_krylov')
# fsolve = LazyImport('from scipy.optimize import fsolve')
# solve_ivp = LazyImport('from scipy.integrate import solve_ivp')
# odeint = LazyImport('from scipy.integrate import odeint')
# # ----------------------------------------

import numpy as np  # NOQA
import pandas as pd  # NOQA
from tqdm import tqdm  # NOQA
from matplotlib import pyplot as plt  # NOQA
import matplotlib as mpl  # NOQA
from cvxopt import umfpack  # NOQA
import cvxopt  # NOQA
import coloredlogs  # NOQA
from multiprocessing import Process  # NOQA

from numpy import ndarray  # NOQA
from cvxopt import spmatrix, matrix, sparse, spdiag  # NOQA

from scipy.optimize import fsolve, newton_krylov  # NOQA
from scipy.integrate import solve_ivp, odeint  # NOQA

pi = 3.14159265358973
jpi2 = 1.5707963267948966j
rad2deg = 57.295779513082323
deg2rad = 0.017453292519943