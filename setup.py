from setuptools import setup, find_packages


setup(
    name='thaumcraft',
    version='0.1',
    description='thaumcraft',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[
        'nose'
    ],
    install_requires=[
        'networkx',
    ],
    entry_points={
        'console_scripts': [
            'main = thaumcraft.main:main',
        ]
    }
)
