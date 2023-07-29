# building our application in to a package, that why we use setup.py seperately
from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path):
    const = "-e ."  # Define the constant here
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if const in requirements:
            requirements.remove(const)
    return requirements


setup(
    name = 'mlproject',
    version = 0.01,
    author='shanu',
    author_email='shanmukharao2952@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)