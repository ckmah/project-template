
# coding: utf-8

# # Analysis Overview
# 
# State the hypothesis/main goal of this notebook.
# 
# #### Background
# 
# 
# #### Hypothesis
# "Synthetic" bulk RNA-seq samples represent heterogeneity within the tumor sample.
# 
# #### Approach
# 1. dimensional reduction
# 2. clustering
# 3. collapse clusters into "synthetic" samples
# 
# #### Dead-ends
# 
# #### Results

# # Notebook Setup

# In[3]:

get_ipython().magic('matplotlib inline')

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

get_ipython().magic('load_ext version_information')


# In[1]:

import warnings
import sys
import os
sys.path.append('../scripts/')

import ipywidgets as widgets
from ipywidgets import interactive, Layout, HTML
from IPython.display import display, Image

from jupyterthemes import jtplot

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import gridspec

import numpy as np
import pandas as pd
import seaborn as sns

from plotly.offline import init_notebook_mode
from plotly import plotly as py
from plotly import graph_objs as go
import cufflinks as cf

sys.path.append('/Users/ckmah/ccal')
import ccal


# In[ ]:

get_ipython().magic('version_information matplotlib,numpy,pandas,seaborn,jupyterthemes,rpy2,biopython,plotly,cufflinks,statsmodels,ipywidgets')


# In[9]:

warnings.filterwarnings('ignore')

jtplot.style()
plt.rcParams['figure.figsize'] = (12,12)
init_notebook_mode()
cf.go_offline()

get_ipython().magic("config InlineBackend.figure_format='retina'")

ccal.VERBOSE = True
sys.setrecursionlimit(20000)


# # Analysis
