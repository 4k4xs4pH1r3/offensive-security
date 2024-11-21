```
conda config --add channels conda-forge && conda create -n x python=3.13 && conda update --all && conda upgrade --all && conda env export > environment.yml && conda deactivate && conda activate x && conda install --file environment.yml && conda update --all && conda upgrade --all
```

```
conda update --all && conda upgrade --all
```


```
python -m ensurepip --upgrade 
```

```
sudo pip list --format=freeze | awk -F '==' '{print $1}' | xargs -n1 pip install -U
```
