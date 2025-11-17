from grgates import GRgates

cdef class FullAdder:
    cdef object g  # usar object si GRgates es Python

    def __init__(self):
        self.g = GRgates()

    cpdef tuple add(self, int A, int B, int Cin):
        cdef int Sum = self.g.gate_xor(self.g.gate_xor(A, B), Cin)
        cdef int Cout = self.g.gate_or(
                            self.g.gate_or(
                                self.g.gate_and(A, B),
                                self.g.gate_and(B, Cin)
                            ),
                            self.g.gate_and(A, Cin)
                        )
        return Sum, Cout
