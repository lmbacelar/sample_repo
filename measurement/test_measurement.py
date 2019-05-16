from mcerp import N, U, Tri
from pytest import approx

from measurement.example_s2 import ExampleS2
from measurement.example_s3 import ExampleS3


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


def test_ea4_2_example_s3():
    m = ExampleS3()
    m.rs = N(10000.053, 0.0025)
    m.delta_rd = U(+0.010, +0.030)
    m.delta_rts = U(-0.00275, +0.00275)
    m.delta_rtx = U(-0.0055, +0.0055)
    m.rc = Tri(0.999_999, 1, 1.000_001)
    m.r = N(1.000_010_5, 0.07e-6)

    assert m.mean == approx(10_000.178, abs=0.001)
    assert m.k() == approx(2.00, rel=0.05)
    assert m.uexp() == approx(0.017, rel=0.05)
