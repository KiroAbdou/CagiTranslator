# setup_env.sh or setup_env.bat
conda env create -f environment.yml
conda activate cagi_env
pip install -r requirements.txt --index-url https://download.pytorch.org/whl/cu118
