import numpy as np
from scipy.optimize import leastsq

#加载数据
ri_data = np.load('ri_data_all.npy').item()
rm_data = np.load('rm_data_all.npy').item()

#对每个行业计算CSAD
def CASD():
    csads = {}
    for k1,v1 in ri_data.items():
        csad = [0]*len(ri_data['玻璃行业']['600176'])
        for k2,v2 in v1.items():
            for i in range(0,len(csad)):
                csad[i] += abs(v2[i]-rm_data[k1][i])/len(v1)
        csads.update({k1:csad})
    return csads

def func(x, p): 
    a, b1, b2 = p
    return a+b1*abs(x)+b2*x*x

def residuals(p, y, x):
    return y - func(x, p)

#非线性回归参数估计
csads = CASD()
for k1,v1 in rm_data.items():
    x = np.array(v1)
    y = np.array(csads[k1])
    p0 = [0, 0, 0] # 待求解的参数的初值
    plsq = leastsq(residuals, p0, args=(y, x)) 
    print(k1,plsq[0])
