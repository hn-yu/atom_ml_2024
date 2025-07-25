from setuptools import setup, find_packages

setup(
    name="curator",
    version="1.1.0",
    description="Library for implementation of message passing neural networks in Pytorch",
    author="xinyang",
    author_email="xinyang@dtu.dk",
    url = "https://github.com/dtu-energy/curator.git",
    packages=find_packages(include=["curator", "curator.*"]),
    scripts=[
        "scripts/curator-train",
        "scripts/curator-tmptrain",
        "scripts/curator-simulate",
        "scripts/curator-select",
        "scripts/curator-label",
        "scripts/curator-deploy",
        "scripts/curator-workflow",
    ],
    install_requires=[
        'myqueue',
        'torch>=1.10',
        'ase',
        'asap3',
        'e3nn',
        'torch-ema>=0.3.0',
        'toml',
        'numpy',
        'hydra-core>=1.2',
        'wandb',
        'lightning',
    ],
    include_package_data=True,
)
