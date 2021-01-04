import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PySimpleFrame",
    version="1.0.0",
    author="Miguel Silva",
    author_email="miguasjpsilva@gmail.com",
    description="",
    long_description=long_description,
    url="https://github.com/OriDevTeam/PySimpleFrame",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC BY-SA 4.0 License",
        "Operating System :: OS Independent",
    ],
)