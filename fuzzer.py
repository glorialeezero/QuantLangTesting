from transpiler import transpile2qiskit, all_close, transpile2cirq
from programs import random_cirq_program, random_qiskit_program
from transformation import inject_op, inject_null_effect_op, inject_reg_op, inject_null_effect_reg
from unitary_gate import generate_random_unitary_gate
import random

def cirq_qiskit_diff_test():
    transpile_fail, suspicious, loop = [], [], 0
    while loop < 1000000:
        loop += 1
        qubit_register = random.randint(3, 10) # circuit size
        
        original = random_cirq_program(qubit_register)
        transpiled = transpile2qiskit(original)
        
        # check if original == tranpiled
        if not all_close(original, transpiled.reverse_bits()):
            transpile_fail.append((original, transpiled))
        else:
            gate_size = random.randint(1, qubit_register) # gate size
            U, U_inv = generate_random_unitary_gate(2 ** gate_size)
            
            # inject null effect register
            original_reg = inject_null_effect_reg(original)
            transpiled_reg = inject_null_effect_reg(transpiled)
            
            # inject null effect operation
            original_null_op = inject_null_effect_op(original, gate_size, U, U_inv)
            transpiled_null_op = inject_null_effect_op(transpiled, gate_size, U, U_inv)
            
            #inject operation
            original_op = inject_op(original, gate_size, U)
            transpiled_op = inject_op(transpiled, gate_size, U)
        
            # check if original' == transpiled'
            if (all_close(original_reg, transpiled_reg.reverse_bits()) 
                and all_close(original_null_op, transpiled_null_op.reverse_bits())
                and all_close(original_op, transpiled_op.reverse_bits())):
                pass
            else:
                suspicious.append((original_op, transpiled_op))

    return transpile_fail, suspicious

def qiskit_cirq_diff_test():
    transpile_fail, suspicious, loop = [], [], 0
    while loop < 10:
        loop += 1
        qubit_register = random.randint(3, 10) # circuit size
        
        original = random_qiskit_program(qubit_register)
        transpiled = transpile2cirq(original)
        
        # check if original == tranpiled
        if not all_close(original.reverse_bits(), transpiled):
            transpile_fail.append((original, transpiled))
        else:
            gate_size = random.randint(1, qubit_register) # gate size
            U, U_inv = generate_random_unitary_gate(2 ** gate_size)
            
            # inject null effect register
            original_reg = inject_null_effect_reg(original)
            transpiled_reg = inject_null_effect_reg(transpiled)
            
            # inject null effect operation
            original_null_op = inject_null_effect_op(original, gate_size, U, U_inv)
            transpiled_null_op = inject_null_effect_op(transpiled, gate_size, U, U_inv)
            
            #inject operation
            original_op = inject_op(original, gate_size, U)
            transpiled_op = inject_op(transpiled, gate_size, U)
        
            # check if original' == transpiled'
            if (all_close(original_reg.reverse_bits(), transpiled_reg)):
                # and all_close(original_null_op.reverse_bits(), transpiled_null_op)
                # and all_close(original_op.reverse_bits(), transpiled_op)):
                pass
            else:
                suspicious.append((original_op, transpiled_op))

    return transpile_fail, suspicious
