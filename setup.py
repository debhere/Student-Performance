from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(filepath:str) -> List[str]:
    '''
    This function loads the requirement file into setup.py
    '''
    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
    if HYPEN_DOT_E in requirements:
        requirements.remove(HYPEN_DOT_E)
    
    return requirements


setup(
    name = "Student Performance",
    version = "0.0.1",
    packages = find_packages(),
    author = "Deb",
    install_requires = get_requirements("requirements.txt")
)