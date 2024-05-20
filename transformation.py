import cirq, copy
from qiskit import QuantumCircuit, QuantumRegister

# Circuit transformation

def inject_op(program, gate_size, U):
    program_prime = copy.deepcopy(program)
    if isinstance(program_prime, QuantumCircuit):
        program_prime.unitary(U, [i for i in range(gate_size-1, -1, -1)])
    elif isinstance(program_prime, cirq.Circuit):
        program_prime.append(cirq.MatrixGate(U)(*[cirq.NamedQubit(str(i)) for i in range(gate_size)]))
    return program_prime

def inject_null_effect_op(program, gate_size, U, U_inv):
    program_prime = copy.deepcopy(program)
    if isinstance(program_prime, QuantumCircuit):
        program_prime.unitary(U, [i for i in range(gate_size)])
        program_prime.unitary(U_inv, [i for i in range(gate_size)])
    elif isinstance(program_prime, cirq.Circuit):
        program_prime.append(cirq.MatrixGate(U)(*[cirq.NamedQubit(str(i)) for i in range(gate_size)]))
        program_prime.append(cirq.MatrixGate(U_inv)(*[cirq.NamedQubit(str(i)) for i in range(gate_size)]))
    return program_prime

def inject_reg_op(program, U):
    program_prime = copy.deepcopy(program)
    if isinstance(program_prime, QuantumCircuit):
        program_prime.add_register(QuantumRegister(1, 'anc'))
        program_prime.unitary(U, QuantumRegister(1, 'anc'))
    elif isinstance(program_prime, cirq.Circuit):
        new_qubit_register = cirq.NamedQubit('anc')
        program_prime.append(cirq.MatrixGate(U)(new_qubit_register))
    return program_prime

def inject_reg_op_multi(program, gate_size, U):
    program_prime = copy.deepcopy(program)
    if isinstance(program_prime, QuantumCircuit):
        anc_reg = QuantumRegister(gate_size, 'anc')
        program_prime.add_register(anc_reg)
        program_prime.unitary(U, reversed(anc_reg))
    elif isinstance(program_prime, cirq.Circuit):
        ancilla_qubits_list = [cirq.NamedQubit(f'anc_{i}') for i in range(gate_size)]
        program_prime.append(cirq.MatrixGate(U)(*ancilla_qubits_list))
    return program_prime

def inject_null_effect_reg(program):
    program_prime = copy.deepcopy(program)
    if isinstance(program_prime, QuantumCircuit):
        program_prime.add_register(QuantumRegister(1, 'anc'))
        program_prime.i(QuantumRegister(1, 'anc'))
    elif isinstance(program_prime, cirq.Circuit):
        new_qubit_register = cirq.NamedQubit('anc')
        program_prime.append(cirq.I(new_qubit_register))
    return program_prime
