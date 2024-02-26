from setuptools import setup,find_packages

setup(
    name = "support",
    version = "0.1.1",
    author = "Sahil Rajwar",
    license = "MIT",
    author_email = "",
    description = "a tiny python library to make things easier",
    packages = find_packages(),
    install_requires = [
        "pandas",
        "numpy"
    ],
    classifiers = [
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Studies",
        "License :: MIT",
        "Programming Language :: Python :: 3"        
    ],
    urls = {
        "https://github.com/Sahil-Rajwar-2004/support"
    }
)
