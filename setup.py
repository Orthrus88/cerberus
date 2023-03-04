# Initial config for setup.py
from setuptools import setup, find_packages

setup(
    name="Cerberus",
    version="0.1.0",
    description="My Python project",
    author="Graham Strom",
    author_email="grahamstrom88@gmail.com",
    url="https://github.com/orthrus88/cerberus",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "torch",
    ],
    extras_require={
        "dev": [
        ]
    },
)
