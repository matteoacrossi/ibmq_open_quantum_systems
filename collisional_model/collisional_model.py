import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def collisional_model(q, system, ancillae, collision_number=None, 
                      g=1., tau=1., measure=False, 
                      environment_qubits=None, **kwargs):
    """Prepare QuantumCircuit for the collisional model
    
        Args: 
            q (QuantumRegister): the register
            system (int): the index of the system qubit
            ancillae (list): the indices of the ancillary qubits
            collision_number (int): number of collisions,
                if None use all qubits in the environment
            g (float): Parameter g for the collision
            tau (float): Parameter tau for the collision
            measure (bool): If True, add X measurement circuit
            environment_qubits (int): Specify how many qubits the system interacts with
            environment_state (string): Specify the initial state of the environment. Can be
            'plus', 'ghz', 'ground'
            
        Returns:
            A QuantumCircuit
        
    """
    
    if environment_qubits is None:
        environment_qubits = len(q) - 1
    else:
        assert environment_qubits <= len(q) - 1, "Not enough qubits in the register" 
        
    if collision_number == None:
        collision_number = environment_qubits
    
    #assert collision_number <= len(e), ("Collision number must be " +
    #"smaller than number of environment qubits")
    
    qc = QuantumCircuit(q)
    
    s = system
    e = ancillae
    
    # Prepare the system in the |+> state
    qc.h(s)

    # Initialize the environment
    prepare_environment(qc, e, **kwargs)

    qc.barrier()
    
    # Collisions with the environment
    for i in range(collision_number):
        collision(qc, g * tau, s, e[i % environment_qubits])

    c = ClassicalRegister(1, name='c')
    if measure:
        qc.add_register(c)
        # Prepare the X measurement circuit
        qc.barrier()
        qc.h(s)
        qc.measure(s, c)
    return qc

def collision(qc, angle, s, e):
    qc.rz(2 * angle, s)
    qc.crz(-4 * angle, e, s)

def coherence(counts):
    """Determine coherence from the counts of X measurement"""
    shots = np.sum([v for v in counts.values()])
    try:
        return 0.5 - counts['1'] / shots
    except KeyError:
        return 0.5 # There where no '1' counts
    
def trace_out_env(state):
    n = int(np.log2(len(state)))
    return partial_trace(state, range(1, n ))

def prepare_environment(qc, e, environment_state='ghz', **kwargs):
    assert environment_state in ('ghz', 'plus', 'ground'), "State can be 'ghz', 'plus' or 'ground'"
    if environment_state == 'ground':
        return qc
    if environment_state == 'ghz':
        qc.h(e[0])
        for i in range(len(e) - 1):
            qc.cx(e[i], e[i+1])
    elif environment_state == 'plus':
        for ek in e:
            qc.h(ek)
    return qc
