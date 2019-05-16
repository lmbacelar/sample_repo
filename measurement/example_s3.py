from .measurement import Measurement


class ExampleS3(Measurement):
    def __init__(
        self,
        rs=0.0,
        delta_rd=0.0,
        delta_rts=0.0,
        rc=0.0,
        r=0.0,
        delta_rtx=0.0,
        npts=10_000,
    ):
        self.rs = rs
        self.delta_rd = delta_rd
        self.delta_rts = delta_rts
        self.rc = rc
        self.r = r
        self.delta_rtx = delta_rtx
        super().__init__(npts)

    @property
    def y(self):
        return (
            self.rs + self.delta_rd + self.delta_rts
        ) * self.rc * self.r - self.delta_rtx
