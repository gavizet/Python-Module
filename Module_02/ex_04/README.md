# Example Package
This is an example package to learn about Python packaging.

# Usage
### Create and activate the virtual env
> \> python -m venv my_env_name && source my_env_name/bin/activate
### Build the package
> \> bash build.sh
### Install the package from source distribution
> \> pip install ./dist/my_minipack-1.0.0.tar.gz
### or Install the package from wheel distribution
> \> pip install ./dist/my_minipack-1.0.0-py3-none-any.whl

# Delete environment
> \> pip freeze > requirements.txt
> 
> \> pip uninstall -r requirements.txt -y
> 
> \> deactivate
> 
> \> rm -r my_env_name

# Documentation
See the [official doc](https://packaging.python.org/en/latest/tutorials/packaging-projects) on how to build packages.

See the [official doc](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools) on how to distribute your package using setuptools.

See this [article](https://python.land/virtual-environments/virtualenv#Why_you_need_virtual_environments) about venv

See this [guide](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/) about python packaging