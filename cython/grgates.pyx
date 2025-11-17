cdef class GRgates:
    # AND
    cpdef int gate_and(self, int a, int b):
        return 1 if a * b == 1 else 0

    # OR
    cpdef int gate_or(self, int a, int b):
        return 1 if a + b >= 1 else 0

    # NOT
    cpdef int gate_not(self, int a):
        return 0 if a == 1 else 1

    # NAND
    cpdef int gate_nand(self, int a, int b):
        return self.gate_not(self.gate_and(a, b))

    # NOR
    cpdef int gate_nor(self, int a, int b):
        return self.gate_not(self.gate_or(a, b))

    # XOR
    cpdef int gate_xor(self, int a, int b):
        return 1 if a != b else 0

    # XNOR
    cpdef int gate_xnor(self, int a, int b):
        return self.gate_not(self.gate_xor(a, b))
