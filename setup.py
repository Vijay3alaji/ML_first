from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this will install every requirements
    '''
    HYPEN_E_DOT = "-e ."
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]
    # check if the line is an -e
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ML_project1',
    version='1.0.0',
    description='practicing Trail nd error',
    author='Vijay',
    author_email='vijaybalajim@sase.ssn.edu.in',
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt'),

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
