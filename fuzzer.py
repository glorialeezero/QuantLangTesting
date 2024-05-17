import random
from transpiler import *

def qiskit_cirq_diff_test():
    suspicious, success, loop = [], [], 0
    while loop < 100:
        loop += 1
        original_prog = random_qiskit_program(random.randint(5, 10))
        transpiled_prog = transpile2cirq(original_prog)
        if not all_close(original_prog, transpiled_prog) and not all_close(original_prog.reverse_bits(), transpiled_prog):
            suspicious.append((original_prog, transpiled_prog))
        else:
            success.append((original_prog, transpiled_prog))
    return suspicious, success

def cirq_qiskit_diff_test():
    suspicious, success, loop = [], [], 0
    while loop < 100:
        loop += 1
        original_prog = random_cirq_program(random.randint(5, 10))
        transpiled_prog = transpile2qiskit(original_prog)
        print(original_prog)
        print(transpiled_prog.draw())
        if not all_close(original_prog, transpiled_prog) and not all_close(original_prog, transpiled_prog.reverse_bits()):
            suspicious.append((original_prog, transpiled_prog))
        else:
            success.append((original_prog, transpiled_prog))
    return suspicious, success

def pyquil_cirq_diff_test():
    suspicious, success, loop = [], [], 0
    while loop < 100:
        loop += 1
        original_prog = random_pyquil_program(random.randint(5, 10))
        transpiled_prog = transpile2cirq(original_prog)
        if not all_close(original_prog, transpiled_prog):
            suspicious.append(original_prog, transpiled_prog)
        else:
            success.append(original_prog, transpiled_prog)
    return suspicious, success
