from mcerp import N, U
import mcerp
import time


class Measurement(object):
    def __init__(self, npts):
        mcerp.npts = npts

    @property
    def y(self):
        pass

    @property
    def mean(self):
        return self.y.mean

    @property
    def std(self):
        return self.y.std

    def uexp(self, prob=0.9545, symmetrical=True):
        lo, mn, _ = self.percentiles(prob, symmetrical)
        return mn - lo

    def k(self, prob=0.9545, symmetrical=True):
        lo, _, hi = self.percentiles(prob, symmetrical)
        return (hi - lo) / (2 * self.std)

    def percentiles(self, prob, symmetrical):
        tail = (1 - prob) / 2
        lo, hi = self.y.percentile([tail, 1 - tail])
        if symmetrical:
            mn = self.mean
            delta = max(mn - lo, hi - mn)
            lo, hi = (mn - delta, mn + delta)
        else:
            mn = (hi - lo) / 2
        return (lo, mn, hi)


class MeasurementExampleS2(Measurement):
    def __init__(self, m_s=0.0, m_d=0.0, delta_m=0.0, m_c=0.0, b=0.0, npts=10_000):
        self.m_s = m_s
        self.m_d = m_d
        self.delta_m = delta_m
        self.m_c = m_c
        self.b = b
        super().__init__(npts)

    @property
    def y(self):
        return self.m_s + self.m_d + self.delta_m + self.m_c + self.b


ti = time.time()

m = MeasurementExampleS2(npts=50_000)
m.m_s = N(10000.005, 0.0225)
m.m_d = U(-0.015, +0.015)
m.delta_m = N(0.020, 0.0144)
m.m_c = U(-0.010, +0.010)
m.b = U(-0.010, +0.010)
m.y

# m.y.describe()
print(m.mean, m.k(), m.uexp())

tf = time.time()

print(tf - ti)
print(mcerp.npts)
