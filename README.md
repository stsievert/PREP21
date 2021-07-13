## Running this notebook
Before class, I'd appreciate if you watched the videos below and got setup with the demo:

1. Install the Anaconda Python distribution: https://www.anaconda.com/products/individual
2. Run these shell commands:

``` shell
$ git clone https://github.com/stsievert/PREP21.git
$ # or download https://github.com/stsievert/PREP21.git
$ cd PREP21
$ conda env create -f env.yaml
$ conda install ipykernel nb_conda_kernels
$ jupyter lab
```

Alternatively, these commands should work:

``` shell
$ pip install numpy scipy scikit-learn pandas seaborn
$ conda install pytorch -c pytorch
$ pip install skorch
$ jupyter lab
```

The Anaconda Navigator can probably be used to install these packages and/or launch environment found in this repository under `env.yaml`.

## Useful links

* https://lucid.wisc.edu/dsworkshop/
