from qiskit import QuantumCircuit, Aer, execute
from qbraid.transpiler import transpile
import cirq

def transpile2cirq(program):
    return transpile(program, "cirq")

def transpile2qiskit(program):
    return transpile(program, "qiskit")

def transpile2qasm2(program):
    return transpile(program, "qasm2")

def transpile2pyquil(program):
    return transpile(program, "pyquil")

def all_close(original_program, transpiled_program):
    original_sv = get_statevector(original_program)
    transpiled_sv = get_statevector(transpiled_program)
    return cirq.allclose_up_to_global_phase(original_sv, transpiled_sv, atol=1e-7)

def get_statevector(program):
    if isinstance(program, QuantumCircuit):
        simulator = Aer.get_backend("statevector_simulator")
        sv = execute(program, simulator).result().get_statevector().data
    elif isinstance(program, cirq.Circuit):
        sv = cirq.final_state_vector(program)
    return sv
