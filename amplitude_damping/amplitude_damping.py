"""
Circuit preparation for the amplitude damping channel
"""

from qiskit import QuantumCircuit
import numpy as np
from scipy.special import xlogy
from scipy.optimize import minimize_scalar

def initial_state(q, sys):
    """Returns a QuantumCircuit implementing the initial condition for the amplitude damping channel
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        sys (int): index for the system qubit
    
    Returns:
        A QuantumCircuit object
    """
    # Create circuit
    ic = QuantumCircuit(q)
    
    # System in |1>
    ic.x(q[sys])
    
    return ic

def initial_state_witness(q, sys, anc):
    """Returns a QuantumCircuit implementing the initial condition for the amplitude damping channel with non-Markovianity witness
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        sys (int): index for the system qubit
        anc (int): index for the ancilla qubit
    
    Returns:
        A QuantumCircuit object
    """
    # Create circuit
    ic = QuantumCircuit(q)
    
    # System and ancilla in |\psi^+>
    ic.h(q[sys])
    ic.cx(q[sys], q[anc])
    
    return ic

def amplitude_damping_channel(q, c, sys, env, R, t):
    """Returns a QuantumCircuit implementing the amplitude damping channel on the system qubit
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        c (ClassicalRegister): the register to use for the measurement of the system qubit
        sys (int): index for the system qubit
        env (int): index for the environment qubit
        R (float): value of R = \gamma_0/\lambda
        t (float): value of the time variable
    
    Returns:
        A QuantumCircuit object
    """
    ad = QuantumCircuit(q, c)
    
    # Rotation angle
    theta = 2.0 * np.arccos(c1(R, t))
    
    # Channel
    ad.cu3(theta, 0.0, 0.0, q[sys], q[env])
    ad.cx(q[env], q[sys])
    
    # Masurement in the computational basis
    ad.measure(q[sys], c[0])
    
    return ad

def amplitude_damping_channel_witness(q, c, sys, env, anc, observable, R, t):
    """Returns a QuantumCircuit implementing the amplitude damping channel on the system qubit with non-Markovianity witness
    
    Args:
        q (QuantumRegister): the register to use for the circuit
        c (ClassicalRegister): the register to use for the measurement of the system and ancilla qubits
        sys (int): index for the system qubit
        env (int): index for the environment qubit
        anc (int): index for the ancillary qubit
        observable (str): the observable to be measured
        R (float): value of R = \gamma_0/\lambda
        t (float): value of the time variable
    
    Returns:
        A QuantumCircuit object
    """
    ad = QuantumCircuit(q, c)
    
    # Rotation angle
    theta = 2.0 * np.arccos(c1(R, t))
    
    # Channel
    ad.cu3(theta, 0.0, 0.0, q[sys], q[env])
    ad.cx(q[env], q[sys])
    
    # Masurement of the corresponding observable
    if observable == 'xx':
        ad.h(sys)
        ad.h(anc)
    elif observable == 'yy':
        ad.sdg(sys)
        ad.h(sys)
        ad.sdg(anc)
        ad.h(anc)
    ad.measure(sys,c[0])
    ad.measure(anc,c[1])
    
    return ad

def c1(R,t):
    """Returns the coherence factor in the amplitude damping channel
    
    Args:
        R (float): value of R = \gamma_0/\lambda
        t (float): value of the time variable
    
    Returns:
        A float number
    """
    
    if R < 0.5:
        c1 = np.exp(- t / 2.0) * (np.cosh(t * np.sqrt(1.0 - 2.0 * R) / 2.0) + 1.0 / np.sqrt(1.0 - 2.0 * R) * np.sinh(t * np.sqrt(1.0 - 2.0 * R) / 2.0))
    else:
        c1 = np.exp(- t / 2.0) * (np.cos(t * np.sqrt(2.0 * R - 1.0) / 2.0) + 1.0 / np.sqrt(2.0 * R - 1.0) * np.sin(t * np.sqrt(2.0 * R - 1.0) / 2.0))
    
    return c1

def H2(p):
    """Returns the binary Shannon entropy of its argument
    
    Args:
        p (float): value of p, between 0 and 1
    
    Returns:
        A float number
    """
    
    H2 = - xlogy(p, p) / np.log(2.0) - xlogy(1.0 - p, 1.0 - p) / np.log(2.0)
    
    return H2

def Qa(c):
    """Returns the quantum channel capacity (Eq. (14) in the paper)
    
    Args:
        c (float): value of |c_1(t)|^2
    
    Returns:
        A float number
    """
    
    Q = 0.0
    if c > 0.5:
        f = lambda p: -H2(c * p) + H2((1.0 - c) * p)
        Q = -minimize_scalar(f, bounds=(0.0, 1.0), method='Bounded').fun
    
    return Q
