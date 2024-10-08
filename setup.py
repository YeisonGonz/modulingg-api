from setuptools import setup, find_packages

setup(
    name='modulingg', 
    version='1.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'modulingg = modulingg.main:main',
        ],
    },
)
