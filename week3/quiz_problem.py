Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> p = np.array([0.3, 0.7, 0.3, 0.7, 0.9, 0.7, 0.3, 0.7, 0.3])
>>> g = np.array([0,1,0,1,1,1,0,1,0])
>>> pg = p * g
>>> p2 = np.square(p)
>>> g2 = np.square(g)
>>> overlap = (2 * pg.sum()) / (p2.sum() + g2.sum())
>>> loss = 1 - overlap
>>> loss
0.0897908979089791
>>> 
