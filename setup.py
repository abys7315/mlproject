from setuptools import find_packages,setup
from typing import List


hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements'''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements
        
        
##metadata about the project
setup(
    name='mlproject',
    version='0.0.1',
    author='Abhay',
    author_email='abys7315@gmail.com',
    packages=find_packages(),#when it will execute it find the package and any folder contain __init__.py file then the folder considered as package
    ##install_requires=['pandas','numpy','seaborn'],#give the libraries whichever is used in project that will automatically install
    install_requires=get_requirements("requirements.txt")
    
)