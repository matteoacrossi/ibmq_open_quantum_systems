# IBM Q Experience as a versatile experimental testbed for simulating open quantum systems

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matteoacrossi/ibmq_open_quantum_systems/master)

A repository with the code used for producing the results of the paper *Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [npj Quantum Inf 6, 1 (2020)](https://doi.org/10.1038/s41534-019-0235-y)*.

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
* [Amplitude damping](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/amplitude_damping/Amplitude_damping_and_channel_capacity.ipynb) reproduces the populations in Fig. 3 and Fig. 5a
* [Amplitude damping with witness](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/amplitude_damping/Amplitude_damping_non-Markovianity_witness.ipynb) reproduces the non-Markovianity witness in Fig. 3
* [Depolarizing channel](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/depolarizing_channel/depolarizing_channel.ipynb) reproduces Fig. 4
* [Extractable work with a Pauli channel](https://nbviewer.jupyter.org/github/matteoacrossi/ibmq_open_quantum_systems/blob/master/pauli_channel/pauli_channel_work_extraction.ipynb) reproduces Fig. 5b

The notebooks can also be used interactively on Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matteoacrossi/ibmq_open_quantum_systems/master)

## Authors and citation
If you find this code useful, please consider citing the paper

*Guillermo García-Peréz, Matteo A. C. Rossi, Sabrina Maniscalco, [npj Quantum Inf 6, 1 (2020)](https://doi.org/10.1038/s41534-019-0235-y).*

BibTeX record:

```
@article{Garcia-Perez2019,
author = {Garc{\'{i}}a-P{\'{e}}rez, Guillermo and Rossi, Matteo A. C. and Maniscalco, Sabrina},
doi = {10.1038/s41534-019-0235-y},
issn = {2056-6387},
journal = {npj Quantum Inf.},
pages = {1},
publisher = {Springer US},
title = {{IBM Q Experience as a versatile experimental testbed for simulating open quantum systems}},
year = {2019}
}
```
