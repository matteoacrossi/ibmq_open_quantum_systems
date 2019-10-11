""" Functions to create the circuit simulating the Pauli channel """

from qiskit import QuantumCircuit
import numpy as np

def pauli_channel_tanh(q, t, system, pauli_ancillae, eta=1, omega=1):
    """Construct the Pauli channel with rates
    
        \\gamma_1(t) = \\eta/2
        \\gamma_2(t) = \\eta/2
        \\gamma_3(t) = -\\omega \\tanh (\\omega t) / 2

    Args:
        q: quantum register
        t (real): time
        system (int): the index of the system qubit
        pauli_ancillae (list): the indices of the two ancillae for the Pauli ch.
        eta (real): parameter
        omega (real): parameter such that omega < eta
        
    Returns:
        a QuantumCircuit
    """

    if np.isclose(t, 0):
        return QuantumCircuit(q)

    # We promote eta and omega to complex or the expression below won't work
    eta = complex(eta)
    omega = complex(omega)

    p = [1/4 * (1 - np.exp(-2 * t *eta)), 
         1/4 * (1 - np.exp(-2 * t *eta)),
         1/4 * (1 + np.exp(-2 * t * eta) - 2 *np.exp(-t *eta) * np.cosh(t *omega))]

    return pauli_channel(q, system, pauli_ancillae, p)

def pauli_channel_tan(q, t, system, pauli_ancillae, eta=1, omega=1):
    """Construct the Pauli channel with rates
    
        \gamma_1(t) = \eta/2
        \gamma_2(t) = \eta/2
        \gamma_3(t) = -\omega \tanh (\omega t) / 2

    Args:
        t (real): time
        eta: parameter
        omega: parameter such that omega < eta
        
    Returns:
        a QuantumCircuit
    """
    
    # We promote eta and omega to complex
    eta = complex(eta)
    omega = complex(omega)
    
    if np.isclose(t, 0): # Just return an emtpy circuit
        return QuantumCircuit(q) 

    p = np.array([1/4 * (1 - np.exp(-2 * t *eta)), 
                  1/4 * (1 - np.exp(-2 * t *eta)),
        1/4 * (1 + np.exp(-2 * t * eta) - 2 *np.exp(-t *eta) * np.cos(t *omega))], dtype=complex)

    return pauli_channel(q, system, pauli_ancillae, p)


def pauli_channel(q, system, pauli_ancillae, p):
    """
        Apply the Pauli channel to system with probabilities p
        (see Eq. (18) of the paper)
    """
    # Make sure p is an array of complex numbers or the next formula will not work
    p = np.array(p, dtype=complex)

    # A solution to Eq. (18)
    c = [np.sqrt(1 - np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2]))))))/np.sqrt(2),
      np.sqrt(8*p[0]**3 - 4*p[0]**2*(-1 - 6*p[2] + np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))))) + 
           (1 - 2*p[2])**2*(-1 + 2*p[2] + np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))))) - 
           2*p[0]*(1 + 4*(p[2] - 3*p[2]**2 - p[2]*np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2]))))) + 
                 np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))*np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2]))))))))/
         (np.sqrt(2)*np.sqrt((-1 + 2*p[0] + 2*p[2])*(4*p[0]**2 + (1 - 2*p[2])**2 + p[0]*(4 + 8*p[2])))),
      np.sqrt((8*p[0]**3 - 4*p[0]**2*(-1 - 6*p[2] + np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))))) + 
             (1 - 2*p[2])**2*(-1 + 2*p[2] + np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))))) - 
             2*p[0]*(1 + 4*(p[2] - 3*p[2]**2 - p[2]*np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2]))))) + 
                   np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2])))*np.sqrt(-4*p[0]**2 + (1 - 2*p[2])**2 + 8*p[0]*(p[2] + np.sqrt(-(p[2]*(-1 + 2*p[0] + p[2]))))))))/
           (4*p[0]**2 + (1 - 2*p[2])**2 + p[0]*(4 + 8*p[2])))/np.sqrt(-2 + 4*p[0] + 4*p[2])]

    theta = 2*np.arccos(np.real(c))

    dc = QuantumCircuit(q)
    dc.ry(theta[0], q[pauli_ancillae[0]])
    dc.cx(q[pauli_ancillae[0]], q[pauli_ancillae[1]])
    dc.ry(theta[1], q[pauli_ancillae[0]])
    dc.ry(theta[2], q[pauli_ancillae[1]])

    dc.cx(q[pauli_ancillae[0]], q[system])
    dc.cy(q[pauli_ancillae[1]], q[system])

    return dc