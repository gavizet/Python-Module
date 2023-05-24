from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

NAME = 'my_minipack'
VERSION = '1.0.0'
DESCRIPTION = 'My first python package, wow'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Gaetan VIZET',
    author_email='gavizet@student.42.fr',
    url=None,
    license='GPLv3',
    keywords='Example little package',
    packages=find_packages(),
    install_requires=[
        'pip',
        'setuptools',
        'wheel'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers - Students",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: >=3.7",
        "Operating System :: Linux",
    ],
    python_requires='>=3.7',

)
