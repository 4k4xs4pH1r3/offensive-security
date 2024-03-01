# Upgrade Pip Script

## Overview

This script is designed to upgrade Python packages using MPI (Message Passing Interface) for parallel processing. It includes functionality to install missing type stubs, upgrade a specific package, and upgrade all installed packages across multiple CPUs.

## Requirements

Install Python 3.x & MPI (Message Passing Interface) accordingly to Your operating system, following this wiki page: https://github.com/4k4xs4pH1r3/offensive-security/tree/master/SuperCluster

## To upgrade Python packages using MPI, execute the following command

   ```bash
   mpirun -v --use-hwthread-cpus python ./upgradepip.py
   ```