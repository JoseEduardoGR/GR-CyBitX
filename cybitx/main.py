# alu_nbit.py

from Mac.grgates import GRgates
from Mac.full_adder import FullAdder

class ALUNBit:
    def __init__(self):
        self.g = GRgates()
        self.fa = FullAdder()

    def operate(self, A: str, B: str, op: str):
        """
        A, B: strings de binario, ej. "10101"
        op: 'AND', 'OR', 'XOR', 'NAND', 'NOR', 'XNOR', 'ADD', 'NOT_A'
        """
        if len(A) != len(B):
            raise ValueError("Los binarios deben tener la misma longitud")

        n = len(A)
        result = ""
        carry = 0

        # Iterar de LSB a MSB
        for i in range(n-1, -1, -1):
            a = int(A[i])
            b = int(B[i])

            if op == 'AND':
                r = self.g.gate_and(a, b)
            elif op == 'OR':
                r = self.g.gate_or(a, b)
            elif op == 'XOR':
                r = self.g.gate_xor(a, b)
            elif op == 'NAND':
                r = self.g.gate_nand(a, b)
            elif op == 'NOR':
                r = self.g.gate_nor(a, b)
            elif op == 'XNOR':
                r = self.g.gate_xnor(a, b)
            elif op == 'ADD':
                r, carry = self.fa.add(a, b, carry)
            elif op == 'NOT_A':
                r = self.g.gate_not(a)
            else:
                raise ValueError("Operación no soportada")

            result = str(r) + result

        # Para ADD, si quedó carry, se puede añadir al inicio
        if op == 'ADD' and carry:
            result = str(carry) + result

        return result
    

alu = ALUNBit()
A = "1010"
B = "0001"

print("AND:", alu.operate(A, B, 'AND'))
print("OR :", alu.operate(A, B, 'OR'))
print("XOR:", alu.operate(A, B, 'XOR'))
print("ADD:", alu.operate(A, B, 'ADD'))