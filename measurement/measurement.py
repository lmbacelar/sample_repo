import mcerp


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
