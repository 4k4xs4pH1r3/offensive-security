conda config --add channels conda-forge
conda create -n x python=3.13
python -m ensurepip --upgrade
conda update --all
conda upgrade --all
conda env export > environment.yml
conda deactivate
conda activate x
conda install --file environment.yml
python -m ensurepip --upgrade
conda update --all
conda upgrade --all
sudo pip list --format=freeze | awk -F '==' '{print $1}' | xargs -n1 pip install -U
