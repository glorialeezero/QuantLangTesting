from pyquil import Program
from pyquil.gates import H, CNOT
from pyquil.api import WavefunctionSimulator

# Initialize the quantum program
p = Program()

# Apply a Hadamard gate to qubit 0
p += H(0)

# Apply a CNOT gate with control qubit 0 and target qubit 1
p += CNOT(0, 1)

# Initialize the WavefunctionSimulator
wfn_sim = WavefunctionSimulator()

# Simulate the program to get the wavefunction (state vector)
wavefunction = wfn_sim.wavefunction(p)

# Print the state vector
print("State vector:")
print(wavefunction)

# Print the amplitudes directly
print("\nAmplitudes:")
print(wavefunction.amplitudes)