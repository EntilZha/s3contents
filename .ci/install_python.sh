#!/usr/bin/env bash

set -e
set -x

# Install miniconda
wget http://repo.continuum.io/miniconda/Miniconda3-3.19.0-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH

conda --version

# Create `test` environment
conda create -n test python=$TRAVIS_PYTHON_VERSION
export PATH=$HOME/miniconda/envs/test/bin:$PATH
pip install pytest pytest-cov python-coveralls