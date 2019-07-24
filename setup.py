from setuptools import setup, find_packages

setup(
    name='ssd',
    version='1.2.0',
    packages=find_packages(include=['ssd.*']),
    install_requires=[
        'torch~=1.0',
        'torchvision~=0.3',
        'opencv-python~=4.0',
        'yacs==0.1.6'
    ]
)
