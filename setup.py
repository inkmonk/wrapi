from setuptools import setup

setup(
    name='wrapi',
    version='0.0.1',
    long_description="A generic API wrapper for python",
    packages=['wrapi'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['requests>=2.6.2']
)
