def ket_expression(statevector, qubit_order='visual'):
    terms = []
    num_qubits = int(statevector.num_qubits)

    for i, amplitude in enumerate(statevector.data):
        if abs(amplitude) > 1e-10:
            bin_state = format(i, f'0{num_qubits}b')
            if qubit_order == 'visual':
                bin_state = bin_state[::-1]
            amp_str = f"{amplitude.real}: .3f" if abs(amplitude.imag) < 1e-10 else f"({amplitude: .3f})"
            terms.append(f"{amp_str}|{bin_state}")
    return " + ".join(terms)