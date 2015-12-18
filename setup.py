from setuptools import setup

setup(
    name='wrapi',
    version='0.0.1',
    description='A generic REST API wrapper',
    long_description="A generic REST API wrapper",
    packages=['wrapi'],
    include_package_data=True,
    install_requires=['requests>=2.6.2'],
    license='MIT',
    author='SuryaSankar',
    author_email='suryashankar.m@gmail.com')
