# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
#package commond : python setup.py sdist
setup(
    name='deepd',
    version='1.0.0',
    description='The deepd project',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    author='Rocky',
    url='https://github.com/rockyCheung/PR.git',
    author_email='274935730@qq.com',
    license='PSF',
    packages=find_packages(),
    install_requires=[''],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'tip': ['*.msg'],
    },
#    include_package_data=False,
    zip_safe=True,
)