from qbraid.interface import circuits_allclose
from qiskit.quantum_info import Operator

from unitary_gate import *
from transformation import *
from transpiler import *
from fuzzer import *
from programs import *


### fuzzer test ####
transpile_fail, suspicious = qiskit_cirq_diff_test()
print(f"transpile_fail: {len(transpile_fail)}")
print(f"suspicious: {len(suspicious)}")

# for i in suspicious:
#     # print(f"original: \n{cirq.dirac_notation(get_statevector(i[0]))}")
#     # print(f"transpiled: \n{cirq.dirac_notation(get_statevector(i[1]))}")
#     print(f"original': \n{i[0]}")
#     print(f"transpiled': \n{i[1]}")


# #### cirq test ####
# program = random_cirq_program(5)
# print(program)
# sv1 = get_statevector(program)
# print(sv1)

# transpiled = transpile2qiskit(copy.deepcopy(program))
# print(transpiled)

# U, U_inv = generate_random_unitary_gate(4)

# program_prime = inject_null_effect_op(program, 2, U, U_inv)
# program_prime = inject_op(program, 2, U)
# program_prime = inject_null_effect_reg(program)
# print(program_prime)

# transpiled_prime = inject_null_effect_op(transpiled, 2, U, U_inv)
# transpiled_prime = inject_op(transpiled, 2, U)
# transpiled_prime = inject_null_effect_reg(transpiled)
# print(transpiled_prime)
# sv_trans_prime = get_statevector(transpiled_prime)
# print(cirq.dirac_notation(sv_trans_prime))

# print(program.all_qubits())
# print(len(program.all_qubits()))
# sv2 = get_statevector(program)
# print(sv2)
# print(cirq.allclose_up_to_global_phase(sv1, sv2, atol=1e-6))
# print(np.allclose(sv1, sv2, atol=1e-6))
