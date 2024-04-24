from setuptools import setup, find_packages

setup(
    name="autocortext_py",
    version="0.1.0",
    description="Simple client for AutoCortext API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Mark Watson",
    author_email="markus.c.watson@gmail.com",
    url="https://autocortext.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "os",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
