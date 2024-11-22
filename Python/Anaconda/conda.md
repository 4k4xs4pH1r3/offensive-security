```
conda update -n base -c conda-forge conda && conda config --add channels conda-forge && conda update --all && conda upgrade --all
```

```
conda env export > environment.yml && conda create -n x python=3.13 && conda deactivate && conda activate x
```

```
conda env update -n x -f environment.yml && conda update --all && conda upgrade --all
```

```
conda update -n base -c conda-forge conda && conda conda update --all && conda upgrade --all
```

```
conda update -n x -c conda-forge conda && conda conda update --all && conda upgrade --all
```

```
conda install -n base conda=24.11.0 && conda install -n x conda=24.11.0
```

```
python -m ensurepip --upgrade
```

```
sudo pip list --format=freeze | awk -F '==' '{print $1}' | xargs -n1 pip install -U
```
