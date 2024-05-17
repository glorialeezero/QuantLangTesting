from fuzzer import *
import pandas as pd
import os

to_check, success = cirq_qiskit_diff_test()
print("To check:", len(to_check))

dataframe = pd.DataFrame({"Qiskit": to_check, "Cirq": to_check})
os.chdir("/Users/ihayeong/Downloads")
dataframe.to_excel("suspicous_programs.xlsx", index=False)