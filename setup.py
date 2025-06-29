#responsible for creating machine learning application as package and deploy in pipi(building applictaion as package)
from setuptools import find_packages, setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements: #will trigeer setup.py automaticalyy -e .
            requirements.remove('-e .')
    return requirements
    
    
setup(
    name='mlproject',
    version='0.0.1',
    author='Manshri',
    author_email='manshri2006@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),
    description='A machine learning project',
)
