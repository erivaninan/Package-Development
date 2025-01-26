from setuptools import setup, find_packages

setup(
    name='part2',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'part2=part2.main:main',
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
