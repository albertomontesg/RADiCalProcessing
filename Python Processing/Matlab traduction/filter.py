
import numpy as np
import scipy.io

def get_filter():
	return scipy.io.loadmat('filter.mat')['fil'][0]
