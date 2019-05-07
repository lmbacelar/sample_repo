from measurement.example_s2 import ExampleS2
import time

from mcerp import N, U

ti = time.time()

m = ExampleS2(npts=30_000)
m.m_s = N(10000.005, 0.0225)
m.m_d = U(-0.015, +0.015)
m.delta_m = N(0.020, 0.0144)
m.m_c = U(-0.010, +0.010)
m.b = U(-0.010, +0.010)
m.y

# m.y.describe()
print(m.mean, m.std, m.k(), m.uexp())

tf = time.time()
print(tf - ti)
