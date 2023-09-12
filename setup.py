from setuptools import setup,find_packages

def get_requirements(file_path):
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","") for r in requirements]
    return requirements


setup(
    name="Project1",
    version="0.0.1",
    description="Pilot Project to understand flow",
    author="Muhammad Nabeel",
    author_email="mnibrahim@cloud.neduet.edu.pk",
    packages=find_packages(),
    install_require = get_requirements('requirements.txt')
)