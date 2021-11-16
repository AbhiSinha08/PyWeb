from setuptools import find_packages, setup

def readme() -> str:
    with open(r"README.md") as f:
        README = f.read()
    return README

setup(
    name='pyweb',
    packages=find_packages(include=['pyweb']),
    version='0.1',
    description='A small Python Library to generate customized static web pages',
    author='Abhinav Sinha',
    author_email="imonline.abhinav@gmail.com",
    url="https://github.com/AbhiSinha08/pyweb",
    license='MIT',
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 1 - Under Development",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)