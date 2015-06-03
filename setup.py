from platform import linux_distribution
from setuptools import setup, find_packages

print(linux_distribution())

def readme():
    with open("README.md") as f:
        return f.read()

def requirements():
    with open("requirements.txt") as f:
        return [s.rstrip("\n") for s in f.readlines() if not s.startswith("#")]

setup(
    name="C3",
    description="CUDA Cloud Computing",
    long_description=readme(),
    author="Pavel Kulyov",
    author_email="kulyov.pavel@gmail.com",
    version="0.1dev",
    py_modules=[],
    packages=find_packages(),
    package_data={},
    license="MIT",
    platforms="Posix",
    install_requires=requirements(),
#        "daemonize",
#        "numpy",
#        "pycuda",
#        "flask",
#        "flask-script",
#    ],
    setup_requires=[
#        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "c3-cns = cns.cns:main",
        ]
    }
)
