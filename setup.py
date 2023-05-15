
from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    """
    :param file_path: requirements.txt
    :return: the list of requirements
    """
    requirements = []
    HYPEN_E_DOT = "-e ."

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]  # remove the "\n" added by readlines()

        if HYPEN_E_DOT in requirements:  # remove "-e ." from the list
            requirements.remove(HYPEN_E_DOT)


setup(
    name='mlproject',
    version='0.0.1',
    author='Gemju Sherpa',
    author_email='gemju.s1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)