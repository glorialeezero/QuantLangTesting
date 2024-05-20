from qiskit.quantum_info import random_unitary
from qbraid.interface import random_unitary_matrix
from numpy.linalg import inv
import numpy as np

# Qbraid
def generate_random_unitary_gate(n):
    U = random_unitary_matrix(n)
    U_inv = inv(U)
    if np.allclose(np.dot(U, U_inv), np.eye(n)) and np.allclose(np.dot(U_inv, U), np.eye(n)):
        return U, U_inv
    else:
        return None

# Qiskit
def generate_random_unitary_gate_qiskit(n):
    U = random_unitary(n).data
    U_inv = U.conj().T
    if np.allclose(np.identity(n), np.dot(U_inv, U)):
        return U, U_inv
    else:
        return None