# IBM Q Experience as a versatile experimental testbed for simulating open quantum systems
A repository of the code used for producing the results of the paper Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [arXiv:1906.07099](https://arxiv.org/abs/1906.07099).

The code is written using [Qiskit](https://github.com/qiskit/qiskit/), and the experiments are run using the free IBM Q Experience.


## Installation and usage
Install the dependencies with

```
pip install -r requirements.txt
```

Clone the repository with

```
git clone https://github.com/matteoacrossi/ibmq_open_quantum_systems.git
```

To run the experiments on the real device, an IBM Q Experience account is needed. Please refer to these [instructions](https://github.com/Qiskit/qiskit-iqx-tutorials/blob/master/INSTALL.md).

## Table of contents
* Reservoir engineering reproduces Fig. 1
* [Collisional model](collisional_model/collisional_model.ipynb) reproduces Fig. 2
* Amplitude damping reproduces Fig. 3 and Fig. 5a
* [Depolarizing channel](depolarizing_channel/depolarizing_channel.ipynb) reproduces Fig. 4
* [Extractable work with a Pauli channel](pauli_channel/pauli_channel_work_extraction.ipynb) reproduces Fig. 5b

## Authors and citation
If you find this code useful 
Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [arXiv:1906.07099](https://arxiv.org/abs/1906.07099).
