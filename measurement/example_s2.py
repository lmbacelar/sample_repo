from .measurement import Measurement


class ExampleS2(Measurement):
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
