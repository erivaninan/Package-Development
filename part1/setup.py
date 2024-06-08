from setuptools import setup, find_packages

setup(
    name='part1',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'part1=part1.main:main',  # Assurez-vous que part1.main contient une fonction main
        ],
    },
    install_requires=[
        'pandas',
        'seaborn',
        'matplotlib',
    ],
    author='Erivan INAN',
    author_email='inanerivan@gmail.com',
    description='Description du package',
    url='https://github.com/erivaninan',
)
