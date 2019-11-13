# IBM Q Experience as a versatile experimental testbed for simulating open quantum systems

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matteoacrossi/ibmq_open_quantum_systems/master)

A repository with the code used for producing the results of the paper Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [arXiv:1906.07099](https://arxiv.org/abs/1906.07099).

The code is written using [Qiskit](https://github.com/qiskit/qiskit/), and the experiments are run using the free IBM Q Experience.

## Installation and usage

Clone the repository with

```
git clone https://github.com/matteoacrossi/ibmq_open_quantum_systems.git
```

Install the dependencies with

```
pip install -r requirements.txt
```

The code was tested with Python 3.7 and qiskit 0.12.

To run the experiments on the real device, an IBM Q Experience account is needed. Please refer to these [instructions](https://github.com/Qiskit/qiskit-iqx-tutorials/blob/master/INSTALL.md).

Each folder contains a Jupyter notebook with a different open quantum system model. 

* [Reservoir engineering](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/reservoir_engineering/Reservoir_engineering.ipynb) reproduces Fig. 1
* [Collisional model](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/collisional_model/collisional_model.ipynb) reproduces Fig. 2
* [Amplitude damping](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/amplitude_damping/Amplitude_damping.ipynb) reproduces Fig. 3 and Fig. 5a
* [Depolarizing channel](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/depolarizing_channel/depolarizing_channel.ipynb) reproduces Fig. 4
* [Extractable work with a Pauli channel](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/pauli_channel/pauli_channel_work_extraction.ipynb) reproduces Fig. 5b

The notebooks can also be used interactively on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matteoacrossi/ibmq_open_quantum_systems/master)

## Authors and citation
If you find this code useful, please cite the paper

Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [arXiv:1906.07099](https://arxiv.org/abs/1906.07099).
