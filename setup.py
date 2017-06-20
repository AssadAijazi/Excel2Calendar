from setuptools import setup, find_packages

with open('LICENSE.txt') as f:
    license = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name="XL2Cal",
    author="Assad Aijazi",
    version='1.0dev',
    packages=find_packages(exclude=['tests']),
    license=license,
    long_description=readme,
    data_files = [('.', ['README.md', 'LICENSE.txt'])],
)
