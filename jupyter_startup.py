# Optional startup script when using Jupyter Notebooks
import os

GLASSNODE_CLIENT_PATH = os.getenv('GLASSNODE_CLIENT_PATH', '/tmp/gn')

import sys
sys.path.append(GLASSNODE_CLIENT_PATH)

# surpress warnings
import warnings
warnings.filterwarnings('ignore')

from glassnode import GlassnodeClient
import matplotlib.pyplot as plt
import pandas as pd

# instantiate glassnode client
gn = GlassnodeClient()

# ipython magic
from IPython import get_ipython
ipython = get_ipython()

if 'ipython' in globals():
    ipython.magic('matplotlib inline')

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (16, 9)
