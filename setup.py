from setuptools import find_packages, setup

def get_requirements() -> list[str]:
    requirements_list: list[str] = []
    # Optionally read from requirements.txt:
    # with open("requirements.txt") as f:
    #     requirements_list = [line.strip() for line in f if line.strip()]
    return requirements_list

setup(
    name='sensor',
    version="0.0.1",
    author="prince",
    author_email="kumarbikky8340@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),  # Or ["pymongo"] if needed
)
