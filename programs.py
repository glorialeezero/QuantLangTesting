import numpy as np
import math
import cirq
from qbraid.interface import random_circuit

# random programs
def random_qiskit_program(n):
    return random_circuit("qiskit", num_qubits=n, depth=n)

def random_cirq_program(n):
    return random_circuit("cirq", num_qubits=n, depth=n)

def random_pyquil_program(n):
    return random_circuit("pyquil", num_qubits=n, depth=n)

# specific programs
def all_superposed(N):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    for i in range(N):
        qc.append(cirq.H(qbits[i]))

    return qc

def ghz(N):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    qc.append(cirq.H(qbits[0]))
    for i in range(1, N):
        qc.append(cirq.CNOT(qbits[0], qbits[i]))

    return qc

def draper_adder(n):  # n for number of bits for a,b
    assert n % 2 == 0
    qbits = cirq.LineQubit.range(n)
    qc = cirq.Circuit()
    
    def R_k_gate(k):
        t = 2 / (2**k)
        return cirq.ZPowGate(exponent=t)

    QFT = cirq.ops.QuantumFourierTransformGate(int(n / 2), without_reverse=True)
    qc.append(cirq.Circuit(QFT(*[qbits[i] for i in range(int(n / 2), n)])))

    for i in range(int(n / 2)):
        for j in range(int(n / 2) - i):
            controlled_R = cirq.ControlledGate(sub_gate=R_k_gate(j + 1), num_controls=1)
            qc.append(controlled_R(qbits[j + i], qbits[int(n / 2) + i]))

    qc.append(cirq.Circuit((QFT**-1)(*[qbits[i] for i in range(int(n / 2), n)])))
    
    return qc

def w_state(N):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    qc.append(cirq.Ry(rads= 2 * np.arccos(math.sqrt((N - 1) / N)))(qbits[0]))
    for i in range(1, N):
        qc.append(
            cirq.ControlledGate(cirq.Ry(rads= 2 * np.arccos(math.sqrt((N - i - 1) / (N - i)))),
                                num_controls= i,
                                control_values= [0] * i)
            (*qbits[:i + 1])
        )
    return qc

def katas_15(N): # katas 1.5
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)
    
    qc.append(cirq.H(qbits[0]))
    for i in range(1,N):
        qc.append(cirq.ControlledGate(
            cirq.ZPowGate(exponent=2 / (2 ** (i + 1))))
            (qbits[i], qbits[0]))

    return qc

def qft(N):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    for i in range(N):
        qc.append(cirq.H(qbits[i]))
        for j in range(i + 1, N):
            qc.append((cirq.CZ ** (1 / 2 ** (j - i)))(qbits[j], qbits[i]))

    return qc

def stack_ww(N):
    assert N % 2 == 0
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    for i in range(N // 2):
        qc.append(cirq.H(qbits[i]))
        qc.append(cirq.CNOT(qbits[i], qbits[i + (N // 2)]))

    return qc

def teleport_step_down(N): # for range decreasing version
    assert N % 3 == 1
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)
    qreg = (N - 1) // 3

    for i in range(qreg, 0, -1):
        qc.append(cirq.H(qbits[qreg + i]))
        qc.append(cirq.CNOT(qbits[qreg + i], qbits[2 * qreg + i]))
        qc.append(cirq.CNOT(qbits[i], qbits[qreg + i]))
        qc.append(cirq.H(qbits[i]))

    return qc

def teleport_step_up(N): # for range increasing version
    assert N % 3 == 1
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)
    qreg = (N - 1) // 3

    for i in range(qreg):
       qc.append(cirq.H(qbits[qreg + i + 1]))
       qc.append(cirq.CNOT(qbits[qreg + i + 1], qbits[2 * qreg + i + 1]))
       qc.append(cirq.CNOT(qbits[i + 1], qbits[qreg + i + 1]))
       qc.append(cirq.H(qbits[i + 1]))
       
    return qc

def odd_or_even_num_superposed(N, bit):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    for i in range(N - 1):
        qc.append(cirq.H(qbits[i]))
    if bit:
        qc.append(cirq.X(qbits[N - 1]))

    return qc

def odd_or_even_num_of_ones(N, bit): # 20_C2
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    for i in range(1, N):
        qc.append(cirq.H(qbits[i]))
        qc.append(cirq.CNOT(qbits[i], qbits[0]))
    if bit:
        qc.append(cirq.X(qbits[0]))

    return qc

def zero_and_bit_superposed(N, bits):
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)

    qc.append(cirq.H(qbits[0]))
    for i in range(1, N):
        if bits[i]:
            qc.append(cirq.CNOT(qbits[0], qbits[i]))

    return qc

def katas_13(N, bits): # katas 1.3
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)
    
    for i in range(N):
        if bits[i] == 1:
            qc.append(cirq.ZPowGate(exponent=2 / (2 ** (i + 1)))(qbits[i]))

    return qc

def two_bits_superposed_pos(N, bits1, bits2): # pos version
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N)
    
    pos = -1
    for i in range(N):
        if bits1[i] != bits2[i]:
            if pos == -1:
                qc.append(cirq.H(qbits[i]))
                pos = i
            else:
                qc.append(cirq.CNOT(qbits[pos], qbits[i]))
        if bits1[i]:
            qc.append(cirq.X(qbits[i]))

    return qc

def two_bits_superposed_anc(N, bits1, bits2): # anc qubit version
    qc = cirq.Circuit()
    qbits = cirq.LineQubit.range(N+1)        
    
    qc.append(cirq.H(qbits[N]))
    
    for i in range(N):
        if bits1[i]:
            qc.append(cirq.ControlledGate(cirq.X, num_controls=1, control_values=[0])(qbits[N], qbits[i]))
        if bits2[i]:
            qc.append(cirq.ControlledGate(cirq.X, num_controls=1, control_values=[1])(qbits[N], qbits[i]))

    qc.append(cirq.ControlledGate(cirq.X, num_controls=N, control_values=bits2)(*qbits[:N+1]))

    return qc
