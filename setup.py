import setuptools

version = '0.7.2'

setuptools.setup(
    name='python-whois-test',
    version='0.1dev',
    packages=[],
    install_requires=[
        'future',
        'whois',
        'pyspark==3.2.2',
        'py4j==0.10.4',
    ],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)