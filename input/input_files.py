# Import libraries
import numpy as np
import scipy.sparse
import scipy.sparse.linalg
import os

import matplotlib.pyplot as plt

from ypstruct import *

# Set-up for finite element analysis
study = struct()
study.meshfile = 'BlaBlaBla'    # Name of mesh-file
study.analysis = 'static'       # Analysis type: (static)

# Print content in the struct study
print('\nInformation\n--------------------------------------------------------------')
print('Mesh-file: '+study.meshfile)
print('Analysis type: '+study.analysis)
print('')


os.chdir('..')
print(os.chdir)
import FEM
