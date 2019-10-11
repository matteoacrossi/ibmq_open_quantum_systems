"""
Circuit preparation for the depolarizing channel
"""

from qiskit import QuantumCircuit
import numpy as np

def depolarizing_channel_3q(q, p, system, ancillae):
    """Returns a QuantumCircuit implementing depolarizing channel on q[system]

    Args:
        q (QuantumRegister): the register to use for the circuit
        p (float): the probability for the channel between 0 and 1
        system (int): index of the system qubit
        ancillae (list): list of indices for the ancillary qubits
        
    Returns:
        A QuantumCircuit object
    """
    dc = QuantumCircuit(q)
   
    theta = 1/2 * np.arccos(1-2*p)
    
    dc.ry(theta, q[ancillae[0]])
    dc.ry(theta, q[ancillae[1]])
    dc.ry(theta, q[ancillae[2]])

    # Prepare q[1] in a maximally mixed state by entangling it with q[0]
    dc.cx(q[ancillae[0]], q[system])
    dc.cy(q[ancillae[1]], q[system])
    dc.cz(q[ancillae[2]], q[system])

    return dc

def depolarizing_channel(q, p):
    """Construct the depolarizing channel

    Args:
        p: probability of the channel
        
    Returns:
        a QuantumCircuit
    """
    
    dc = QuantumCircuit(q)
    
    assert 0 <= p <= 1, "p must be 0 <= p <= 1"

    # If p = 0 then do nothing
    if np.isclose(p, 0):
        return dc
    if p == 1:
        c = [1/np.sqrt(2), np.sqrt(2 + np.sqrt(2))/2, np.sqrt(2 + np.sqrt(2))/2]
    else:
        p = complex(p)
        c = [np.sqrt(-4 - 2*np.sqrt(2)*np.sqrt((2 + (-2 + p)*p + 
            np.sqrt((4 - 3*p)*p**3))/(1 + p**2)) - 
            np.sqrt(2)*p**2*np.sqrt((2 + (-2 + p)*p + 
            np.sqrt((4 - 3*p)*p**3))/(1 + p**2)) + 
            np.sqrt(2)*np.sqrt((4 - 3*p)*p**3)*np.sqrt((2 + (-2 + p)*p +
            np.sqrt((4 - 3*p)*p**3))/(1 + p**2)) + 
            2*p*(2 + np.sqrt(2)*np.sqrt((2 + (-2 + p)*p + 
            np.sqrt((4 - 3*p)*p**3))/(1 + p**2))))/(2.*np.sqrt(2)*np.sqrt(-1 + p)),
            -np.sqrt(2 + np.sqrt(2)*np.sqrt((2 + (-2 + p)*p + np.sqrt((4 - 3*p)*p**3))/(1 + p**2)))/2.,
            -np.sqrt(2 + np.sqrt(2)*np.sqrt((2 + (-2 + p)*p + np.sqrt((4 - 3*p)*p**3))/(1 + p**2)))/2.]

    theta = 2*np.arccos(np.real(c))
    
    dc.ry(theta[0], q[3])
    dc.cx(q[3],q[4])
    dc.ry(theta[1], q[3])
    dc.ry(theta[2], q[4])

    # Prepare q[1] in a maximally mixed state by entangling it with q[0]
    dc.cx(q[3], q[2])
    dc.cy(q[4], q[2])

    return dc