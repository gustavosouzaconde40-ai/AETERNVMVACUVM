from setuptools import setup, find_packages

setup(
    name="aeternvmvacuvm",
    version="1.0.0",
    author="Gustavo Alves Condé",
    author_email="gustavosouzaconde@hotmail.com",
    description="Framework computacional para transicoes de fase do vacuo e emuladores cosmologicos.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
