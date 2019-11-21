"""
Circuit preparation for the markovian reservoir engineering
"""

from qiskit import QuantumCircuit
import numpy as np

def initial_conditions(q, system):
    """Returns a dictionary containing four QuantumCircuit objects which prepare the two-qubit system in different initial states
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        system (list): list of indices for the system qubits
    
    Returns:
        A dictionary with the initial state QuantumCircuit objects and a list of labels
    """
    # State labels
    state_labels = ['00', '01', '10', '11']
    
    ic = {}
    for ic_label in state_labels:
        ic[ic_label] = QuantumCircuit(q)
    
    # |01>
    ic['01'].x(q[system[0]])
    
    # |10>
    ic['10'].x(q[system[1]])
    
    # |11>
    ic['11'].x(q[system[0]])
    ic['11'].x(q[system[1]])
    
    return ic, state_labels

def zz_pump(q, c, p, system, ancilla):
    """Returns a QuantumCircuit implementing the ZZ pump channel on the system qubits
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        c (ClassicalRegister): the register to use for the measurement of the system qubits
        p (float): the efficiency for the channel, between 0 and 1
        system (list): list of indices for the system qubits
        ancilla (int): index for the ancillary qubit
    
    Returns:
        A QuantumCircuit object
    """
    zz = QuantumCircuit(q, c)
    
    theta = 2 * np.arcsin(np.sqrt(p))
    
    # Map information to ancilla
    zz.cx(q[system[0]], q[system[1]])
    zz.x(q[ancilla])
    zz.cx(q[system][1], q[ancilla])
    
    # Conditional rotation
    zz.cu3(theta, 0.0, 0.0, q[ancilla], q[system[1]])
    
    # Inverse mapping
    zz.cx(q[system[1]], q[ancilla])
    
    # Measurement
    zz.h(q[system[0]])
    zz.measure(q[system[0]], c[0])
    zz.measure(q[system[1]], c[1])
    
    return zz

def xx_pump(q, c, p, system, ancilla):
    """Returns a QuantumCircuit implementing the XX pump channel on the system qubits
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        c (ClassicalRegister): the register to use for the measurement of the system qubits
        p (float): the efficiency for the channel, between 0 and 1
        system (list): list of indices for the system qubits
        ancilla (int): index for the ancillary qubit
    
    Returns:
        A QuantumCircuit object
    """
    xx = QuantumCircuit(q, c)

    theta = 2 * np.arcsin(np.sqrt(p))
    
    # Map information to ancilla
    xx.cx(q[system[0]], q[system[1]])
    xx.h(q[system[0]])
    xx.x(q[ancilla])
    xx.cx(q[system[0]], q[ancilla])
    
    # Conditional rotation
    xx.cu3(theta, 0.0, 0.0, q[ancilla], q[system[0]])
    
    # Inverse mapping
    xx.cx(q[system[0]], q[ancilla])
    
    # Measurement
    xx.measure(q[system[0]], c[0])
    xx.measure(q[system[1]], c[1])
    
    return xx

def zz_xx_pump(q, c, p, system, ancillae):
    """Returns a QuantumCircuit implementing the composition channel on the system qubits
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        c (ClassicalRegister): the register to use for the measurement of the system qubits
        p (float): the efficiency for both channels, between 0 and 1
        system (list): list of indices for the system qubits
        ancillae (list): list of indices for the ancillary qubits
    
    Returns:
        A QuantumCircuit object
    """
    zx = QuantumCircuit(q, c)
    
    theta = 2 * np.arcsin(np.sqrt(p))
    
    # ZZ pump
    ## Map information to ancilla
    zx.cx(q[system[0]], q[system[1]])
    zx.x(q[ancillae[0]])
    zx.cx(q[system[1]], q[ancillae[0]])
    
    ## Conditional rotation
    zx.cu3(theta, 0.0, 0.0, q[ancillae[0]], q[system[1]])
    
    ## Inverse mapping
    zx.cx(q[system[1]], q[ancillae[0]])
    
    # XX pump
    ## Map information to ancilla
    zx.h(q[system[0]])
    zx.x(q[ancillae[1]])
    zx.cx(q[system[0]], q[ancillae[1]])
    
    ## Conditional rotation
    zx.cu3(theta, 0.0, 0.0, q[ancillae[1]], q[system[0]])
    
    ## Inverse mapping
    zx.cx(q[system[0]], q[ancillae[1]])
    
    # Measurement
    zx.measure(q[system[0]], c[0])
    zx.measure(q[system[1]], c[1])
    
    return zx
