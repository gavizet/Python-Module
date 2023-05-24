
# Upgrade desired packages with venv python version
python -m pip install --upgrade pip setuptools wheel

# Create the package from the setup.py file
# sdist is for the source distribution
# bdist_wheel is for the wheel distribution
python setup.py sdist bdist_wheel

echo; echo