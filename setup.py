from setuptools import setup, find_packages

setup(
    name='modulingg',
    version='1.4.0',
    packages=['modulingg'],
    install_requires=[
        "fastapi[standard]",
    ],
    entry_points={
        'console_scripts': [
            'modulingg = modulingg.main:main',
        ],
    },
)
