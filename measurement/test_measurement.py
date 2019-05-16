from mcerp import N, U
from pytest import approx

from measurement.example_s2 import ExampleS2


def test_ea4_2_example_s2():
    m = ExampleS2()
    m.m_s = N(10000.005, 0.0225)
    m.m_d = U(-0.015, +0.015)
    m.delta_m = N(0.020, 0.0144)
    m.m_c = U(-0.010, +0.010)
    m.b = U(-0.010, +0.010)

    assert m.mean == approx(10000.025, abs=0.001)
    assert m.k() == approx(2.00, rel=0.05)
    assert m.uexp() == approx(0.059, rel=0.05)
